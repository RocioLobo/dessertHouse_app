import reflex as rx
def postresfaciles() -> rx.Component:
    return rx.vstack(
        rx.heading("Postres Fáciles", size="4"),
        rx.text("Aquí encontrarás recetas de postres fáciles de preparar."),
        rx.link("Regresar al inicio", href="/"),
        spacing="4",
        padding="4"
    )