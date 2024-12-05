"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# Definimos la pantalla de inicio

def homepage():
    return rx.box(
        rx.text(
            "¡Bienvenido a DessertHouse!",
            font_size="3xl",
            font_weight="bold",
            margin_bottom="1em",
            color="black",
        ),
        # rx.image(
        #     src=rx.image(src="/logo.https://trello.com/1/cards/672e49f8b0bb11b91a971201/attachments/674483f200f7d2fffd17848b/previews/674483f300f7d2fffd1787c2/download/Dessert.webp"),  
        #     width="200px",
        #     margin_bottom="1em",
        # ),
        rx.button(
            "Registrarse",
            # on_click=rx.route.register("/register"),
            background="green",
            color="black",
            padding="1em",
            margin_bottom="1em",
            border_radius="8px",
        ),
        rx.button(
            "Iniciar Sesión",
            # on_click=rx.route.login("/login"),
            background="blue",
            color="black",
            padding="1em",
            border_radius="8px",
        ),
        align="center",
        justify="center",
        height="100vh",
        background="linear-gradient(to bottom,#f70071 )",
    )