"""Welcome to Reflex! This file outlines the steps to create a basic app."""
# Definimos la página (login  como ejemplo)
import reflex as rx


def loginpage()->rx.Component:
    return rx.box(
        rx.text(
            "Iniciar Sesión",
            font_size="2xl",
            font_weight="bold",
            margin_bottom="1em",
        ),
        rx.input(placeholder="Usuario", margin_bottom="1em", width="300px"),
        rx.input(placeholder="Contraseña", type="password", margin_bottom="1em", width="300px"),
        rx.button(
            "Iniciar Sesión",
            # on_click=lambda: print("Usuario autenticado"),
            background="white",
            color="black",
            padding="1em",
            border_radius="8px",
        ),
        align="center",
        justify="center",
        height="100vh",
        spacing="4"
    )