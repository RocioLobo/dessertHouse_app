"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from.pages.home import HomePage  # Importa la pantalla de inicio
# from dessertHouse_app.login import LoginPage  # Importa la pantalla de login
# from dessertHouse_app.register import RegisterPage  # Importa la pantalla de registro

# # Define las rutas de las páginas
# def index():
#     return HomePage()
# def index():
#     return LoginPage()
# def index():
#     return RegisterPage()

#crea la instancia de la aplicacion
app =rx.App()
# Inicializamos la aplicación
app.add_page(route="/", component=HomePage)           # Ruta principal
# app.add_page(route="/login", component=LoginPage)  # Ruta para la pantalla de login
# app.add_page(route="/register", component=RegisterPage)  # Ruta para registro
