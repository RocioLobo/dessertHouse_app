"""Welcome to Reflex! This file outlines the steps to create a basic app."""
# Definimos la página (register como ejemplo)

import reflex as rx

def registerpage()-> rx.Component:
    return rx.box(
        rx.text(
            "Crear una Cuenta",
            font_size="2xl",
            font_weight="bold",
            margin_bottom="1em",
        ),
        rx.input(placeholder="Nombre", margin_bottom="1em", width="300px"),
        rx.input(placeholder="Correo Electrónico", margin_bottom="1em", width="300px"),
        rx.input(placeholder="Contraseña", type="password", margin_bottom="1em", width="300px"),
        rx.button(
            "Registrarse",
            # on_click=lambda: print("Usuario registrado"),
            background="green",
            color="white",
            padding="1em",
            border_radius="8px",
        ),
        align="center",
        justify="center",
        height="100vh",
        spacing="4"
    )