from django.urls import path
from .views import pokemon_list, pokemon_detail, signup, signout, signin

urlpatterns = [
    path('', pokemon_list, name= 'pokemons'),
    path('pokemon/<int:pokemon_id>/',pokemon_detail, name='pokemon_detail'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name="signout"),
    
]
