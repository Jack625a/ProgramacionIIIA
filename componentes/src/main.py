import flet as ft


def main(page: ft.Page):
    
    page.add(
        ft.Text("Prueba",size=30,color=ft.colors.RED),
        ft.Image(src="https://media.licdn.com/dms/image/v2/D4D10AQHV1zAGFoIGuw/image-shrink_800/image-shrink_800/0/1693488545613?e=2147483647&v=beta&t=Jvu3F1SeVz3tYkUgmFUCCFmJBSER8V5jIM2R-2FosAA", width=250,border_radius=20),
        ft.Image(src="componentes/src/assets/1pyt.jpg", width=200),
        ft.Button(text="Boton 1",icon=ft.Icons.HOME),
        ft.CupertinoButton(text="Boton 2",icon=ft.Icons.FACE),
        ft.CupertinoFilledButton(text="Boton 3",icon=ft.Icons.STORE),
        ft.OutlinedButton(text="Boton 4"),
        ft.FilledButton(text="Botn 5"),
        ft.IconButton(icon=ft.Icons.PANORAMA),
        
    )


ft.app(main)
