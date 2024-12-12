"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# Definimos la pantalla de inicio

def homepage()-> rx.Component:
    return rx.box(
        rx.text("¡Bienvenido a DessertHouse!"),
        rx.container,
        rx.heading("App contador"),
        size="4",
        align="center",
        color="#000000",
    )
        
    
    #     rx.text(
    #         "¡Bienvenido a DessertHouse!",
    #         font_size="3xl",
    #         font_weight="bold",
    #         margin_bottom="1em",
    #         color="white",
    #         text_aling="center",

    #     ),
    #     # rx.image(
    #     #     src=rx.image(src="/logo.https://trello.com/1/cards/672e49f8b0bb11b91a971201/attachments/674483f200f7d2fffd17848b/previews/674483f300f7d2fffd1787c2/download/Dessert.webp"),  
    #     #     width="200px",
    #     #     margin_bottom="1em",
    #     # ),
# rx.vstack(
#     rx.button(
#         "Registrarse",
#             # on_click=rx.route.register("/register"),
#             background="white",
#             color="black",
#             padding="1em",
#             margin_bottom="1em",
#             border_radius="8px",
#             aling="center",
#  ),
    #         rx.button(
    #             "Iniciar Sesión",
    #             # on_click=rx.route.login("/login"),
    #             background="white",
    #             color="black",
    #             padding="1em",
    #             border_radius="8px",
    #         ),
    #     ),
    #     align="center",
    #     justify="center",
    #     height="100vh",
    #     background="#df0064",
    #     spacing="5",
    # )