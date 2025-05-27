import flet as ft

def opcion2():
    return ft.Container(
        content=ft.Column([
                ft.Text("Contenido Pantalla 2",size=30),
                ft.Text("Pantalla 2.",size=16,color=ft.Colors.DEEP_PURPLE_700)
        ])
        
    )