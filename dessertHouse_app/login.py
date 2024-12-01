"""Welcome to Reflex! This file outlines the steps to create a basic app."""
# Definimos la página (login  como ejemplo)
import reflex as rx


def login_page():
    return rx.center(
        rx.text("Página de inicio de sesión", font_size="2xl")
    )