import reflex as rx
def Extras() -> rx.Component:
    return rx.vstack(
        rx.heading("Extras", size="4"),
        rx.text("Aquí encontrarás recetas y consejos adicionales."),
        rx.link("Regresar al inicio", href="/"),
        spacing="4",
        padding="4"
    )