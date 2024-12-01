"""Welcome to Reflex! This file outlines the steps to create a basic app."""
# Definimos la página (register como ejemplo)

import reflex as rx

def register_page():
    return rx.center(
        rx.text("Página de registro", font_size="2xl")
    )
