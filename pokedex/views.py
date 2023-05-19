from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import re



# Create your views here.

#----------------------- consumir la API --------------
def pokemon_list(request):
    pokemones= []
    pokemones_consultados= requests.get("https://pokeapi.co/api/v2/pokemon")
    pokemones_consultados=pokemones_consultados.json()
    pokemones = pokemones + pokemones_consultados["results"]
    while "next" in pokemones_consultados.keys() and pokemones_consultados["next"] != None:
        pokemones_consultados = requests.get(pokemones_consultados["next"])
        pokemones_consultados = pokemones_consultados.json()
        pokemones = pokemones + pokemones_consultados["results"]
    
    # Obtener los detalles de cada Pokémon
    for pokemon in pokemones:
        #extrae el ID de la URL de cada pokémon y lo asigna como un nuevo campo llamado "id" en el diccionario del pokemon
        pokemon["id"] = re.findall(r'\d+', pokemon["url"])[-1]
    
    context = {"pokemones": pokemones}
    return render(request, "pokemons.html", context)

@login_required
def pokemon_detail(request, pokemon_id):
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(pokemon_url)
    #verifica si la solicitud al servicio de la API para obtener los detalles del Pokemon fue exitosa
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_details = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "image_url": pokemon_data["sprites"]["front_default"],
            "type": pokemon_data["types"][0]["type"]["name"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            # Agrega otros detalles del Pokémon que desees mostrar
        }
        context = {"pokemon": pokemon_details}
        return render(request, "pokemon_detail.html", context)
    else:
        return HttpResponse("Error: Error al obtener los detalles de Pokemon")

#---------- registro ----------------

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('pokemons')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "El usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})

#-----------cerrar sesion-----------------
@login_required
def signout(request):
    logout(request)
    return redirect('pokemons')


#-----------iniciar sesion-----------------
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Usuario o contraseña incorrecta."})

        login(request, user)
        return redirect('pokemons')