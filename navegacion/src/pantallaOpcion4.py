import flet as ft

def opcion4():
    return ft.Container(
        content=ft.Column([
                ft.Text("Contenido Pantalla 4",size=30),
                ft.Text("Pantalla 4.",size=16,color=ft.Colors.DEEP_PURPLE_700),
                ft.Checkbox(label="seleccionar")
        ])
        
    )