import reflex as rx
def Consejos() -> rx.Component:
    return rx.vstack(
        rx.heading("Consejos", size="4"),
        rx.text("Consejos útiles para hacer postres."),
        rx.link("Regresar al inicio", href="/"),
        spacing="4",
        padding="4"
    )