"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from.pages.home import homepage  # Importa la pantalla de inicio
from.pages.login import loginpage  # Importa la pantalla de login
from.pages.register import registerpage# Importa la pantalla de registro
from.pages.postres_faciles import postresfaciles  # Importa la categoria postres faciles
from.pages.postres_frios import postresfrios 
from.pages.postres_rapidos import postresrapidos
from.pages.consejos import Consejos
from.pages.extras import Extras

# from.pages.language import languagepage  # Importa la pantalla de lenguage


# # Define las rutas de las páginas
# def index()
#     return homepage()
# def index():
#     return loginpage()
# def index():
#     return registerpage()

#crea la instancia de la aplicacion
app =rx.App()
# Inicializamos la aplicación
app.add_page(route="/", component=homepage)           # Ruta principal
app.add_page(route="/login", component=loginpage)     # Ruta para la pantalla de login
app.add_page(route="/register", component=registerpage)  # Ruta para registro
# app.add_page(route="/language", component=languagepage)  # Ruta para lenguage
app.add_page(route="/postres_faciles", component=postresfaciles)
app.add_page(route="/postres_rapidos", component=postresrapidos)
app.add_page(route="/postres_frios", component=postresfrios)
app.add_page(route="/consejos", component=Consejos)
app.add_page(route="/extras", component=Extras)