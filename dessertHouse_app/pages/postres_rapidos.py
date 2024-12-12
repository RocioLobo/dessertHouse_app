import reflex as rx
def postresrapidos() -> rx.Component:
    return rx.vstack(
        rx.heading("Postres Rápidos", size="4"),
        rx.text("Aquí encontrarás recetas de postres que puedes hacer rápidamente."),
        rx.link("Regresar al inicio", href="/"),
        spacing="4",
        padding="4"
    )