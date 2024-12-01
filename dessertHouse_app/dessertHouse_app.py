"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from dessertHouse_app.home import HomePage  # Importa la pantalla de inicio
from dessertHouse_app.login import LoginPage  # Importa la pantalla de login
from dessertHouse_app.register import RegisterPage  # Importa la pantalla de registro

# Define las rutas de las páginas
def index():
    return HomePage()
def index():
    return LoginPage()
def index():
    return RegisterPage()

# Inicializamos la aplicación
app = rx.App()
app.add_page(index, route="/")           # Ruta principal
app.add_page(LoginPage, route="/login")  # Ruta para la pantalla de login
app.add_page(RegisterPage, route="/register")  # Ruta para registro
app.compile()