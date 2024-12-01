"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from home import home_page  
from login import login_page
from register import register_page

# Define las rutas de la aplicación
def index():
    return home_page()
def index():
    return login_page()
def index():
    return register_page()


# Configura la aplicación
app = rx.App()
app.add_page(index, route="/")  # Página principal
app.compile()


# Inicializamos la app
app = rx.App()
app.add_page(index)