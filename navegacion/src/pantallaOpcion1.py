#importar flet

import flet as ft

def opcion1():
    return ft.Container(
        content=ft.Column([
                ft.Text("Contenido Pantalla 1",size=30),
                ft.Text("Pantalla 1.",size=16,color=ft.Colors.DEEP_PURPLE_700)
        ])
        
    )
    


