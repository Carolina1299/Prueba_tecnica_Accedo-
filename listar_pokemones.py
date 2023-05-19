import requests

pokemones= []
pokemones_consultados= requests.get("https://pokeapi.co/api/v2/pokemon")
pokemones_consultados=pokemones_consultados.json()
pokemones = pokemones + pokemones_consultados ["results"]
while "next" in pokemones_consultados-keys and pokemones_consultados ["next"] != None:
    pokemones_consultados = requests.get(pokemones_consultados["next"])
    pokemones_consultados = pokemones_consultados.json()
    pokemones = pokemones + pokemones_consultados ["results"]

print(pokemones) 