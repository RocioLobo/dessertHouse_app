"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

def languagepage()->rx.component:
    return rx.Box(
        children=[
            rx.Text("Idioma / Language", font_size="20px", font_weight="bold", margin_bottom="20px"),
            rx.Box(
                children=[
                    rx.Button("Español", on_click=lambda: print("Idioma seleccionado: Español")),
                    rx.Button("English", on_click=lambda: print("Language selected: English")),
                    rx.Button("Extras", on_click=lambda: print("Extras selected")),
                ],
                display="flex",
                flex_direction="column",
                align_items="center",
                gap="10px",
            ),
        ],
        padding="20px",
        align_items="center",
        justify_content="center",
        background_color="#f0f0f0",
        height="100vh",
    )