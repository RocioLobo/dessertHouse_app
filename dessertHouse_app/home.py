"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


# Definimos la pantalla de inicio
def home_page():
    return rx.center(
        rx.vstack(
            rx.text("¡Bienvenido a desserthouse!", font_size="3xl", font_weight="bold"),
            rx.text("podras aprender a preparar  postres con recetas de casa ¡vuelvete la mejor repostera! .", font_size="lg"),
            rx.button("Iniciar sesión", on_click="/login", color="blue", size="lg"),
            rx.button("Registrarse", on_click="/register", color="green", size="lg"),
            spacing="20px",
        ),
        height="100vh",  # Altura total de la pantalla
        bg="lightgray",  # Fondo de la pantalla
    )