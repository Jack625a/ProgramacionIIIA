#Importacion del framework
import flet as ft

#importacion de pantallas 
from pantallaOpcion1 import opcion1
from pantallaOpcion2 import opcion2
from pantallaOpcion3 import opcion3
from pantallaOpcion4 import opcion4


#Funcion principal
def main(page: ft.Page):
    
    #PASO 1. DEFINIR LA VARIABLE NAVEGACION
    navegacion=ft.Tabs(
        tabs=[
            ft.Tab(
                text="Opcion 1",
                icon=ft.Icons.HOME,
                content=opcion1()
            ),
            ft.Tab(
                text="Opcion 2",
                icon=ft.Icons.PHONE_IN_TALK,
                content=opcion2()
    
            ),
            ft.Tab(
                text="Opcion 3",
                icon=ft.Icons.QUEUE_SHARP,
                content=opcion3()
            ),
            ft.Tab(
                text="Opcion 4",
                icon=ft.Icons.TIKTOK,
                content=opcion4()
            )

        ],
        expand=1
        
        )


    #TOD. LO QUE SE VERA EN LA INTERFAZ
    page.add(
        navegacion  
    )


ft.app(main)
