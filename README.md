# Pokedex

Este proyecto es una aplicación web que simula una Pokedex, una enciclopedia de Pokémon. Permite a los usuarios explorar una lista de Pokémon y ver detalles de cada uno.

## Características

- Lista de Pokémon: Muestra una lista de Pokémon con su nombre y enlaces a los detalles de cada uno.
- Detalles del Pokémon: Permite ver información detallada de cada Pokémon, como su nombre, imagen, altura, peso. Restricción: el usuario debe estar logueado para poder ver los detalles del Pokémon.
- Registro e inicio de sesión: Los usuarios deben registrarse e iniciar sesión para poder ver los detalles del Pokémon.

## Tecnologías utilizadas

- Django: Framework de desarrollo web utilizado para el backend de la aplicación.
- HTML/CSS: Lenguajes de marcado utilizados para la estructura y estilo de las páginas web.
- Tailwind CSS: Framework CSS utilizado para agilizar el diseño y la apariencia de la interfaz de usuario.
- PokeAPI: API utilizada para obtener información de los Pokémon, como sus detalles y características.

## Instalación
1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual y actívalo.
3. Instala las dependencias del proyecto utilizando pip install -r requirements.txt.
4. Configura la conexión a la base de datos en el archivo settings.py.
5. Ejecuta las migraciones de la base de datos utilizando python manage.py migrate.
6. Inicia el servidor de desarrollo con python manage.py runserver.
7. Abre tu navegador y visita http://localhost:8000 para acceder a la aplicación Pokedex.