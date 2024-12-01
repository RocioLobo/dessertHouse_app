"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


# Definimos la pantalla de inicio
import reflex as rx

def HomePage():
    return rx.box(
        rx.text(
            "¡Bienvenido a Dessert House!",
            font_size="3xl",
            font_weight="bold",
            margin_bottom="1em",
        ),
        rx.image(
            src="https://trello.com/c/k22u9Xhf/17-crear-mi-logo-de-mi-app",  # Cambia este archivo por tu logo si lo tienes
            width="200px",
            margin_bottom="1em",
        ),
        rx.button(
            "Registrarse",
            on_click=rx.route("/register"),
            background="green",
            color="white",
            padding="1em",
            margin_bottom="1em",
            border_radius="8px",
        ),
        rx.button(
            "Iniciar Sesión",
            on_click=rx.route("/login"),
            background="blue",
            color="white",
            padding="1em",
            border_radius="8px",
        ),
        align="center",
        justify="center",
        height="100vh",
        background="linear-gradient(to bottom, #f9d423, #ff4e50)",
    )