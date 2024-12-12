import reflex as rx
def postresfrios() -> rx.Component:
    return rx.vstack(
        rx.heading("Postres Fríos", size="4"),
        rx.text("Aquí encontrarás recetas de postres fríos."),
        rx.link("Regresar al inicio", href="/"),
        spacing="4",
        padding="4"
    )