#LIBRERIAS
import flet as ft #FLET
import requests

#PASO1. CREDENCIALES DE AIRTABLE
tokenAirtable=''
idBaseDato=''
nombreBasedatos=''
HEADERS={
    "Authorization": f"Bearer {tokenAirtable}",
    "Content-Type":"application/json"
}
urlConexion=f'https://api.airtable.com/v0/{idBaseDato}/{nombreBasedatos}'

#PASO 2 CREAR LA FUNCION PARA OBTNER LOS DATOS
def obtenerDatos():
    try:
        respuesta=requests.get(urlConexion, headers=HEADERS)
        if respuesta.status_code==200:
            return respuesta.json().get("records",[])
        else: 
            print("Error al obtener los datos ",respuesta.text)
            return []
    except Exception as e:
        print("Error al autentificar ", e)
        return []
        
#funcion para agregar datos

def main(page: ft.Page):

    page.title="Conexion base de datos"
    page.scroll="AUTO"

    resultado=ft.Text("Estudiantes registros")
    contenedorChips=ft.Row(wrap=True)
    nombreBD=ft.ListView(expand=True)
    carrera=ft.Text("")
    edad=ft.Text("")

    #PASO 3. MOSTRAR LOS DATOS
    def mostrarDatos(e):
        datos=obtenerDatos()
        print(datos)
        if not datos:
            resultado.value="No se tienen datos en la base de datos!!!"
        else:
            datosEstudiante="Lista de estudiante"
            nombreObtenido=[]
            for item in datos:
                fields=item.get("fields",{})
                nombre=fields.get("Nombre","Sin nombre")
                carrera=fields.get("Carrera","Sin carrera")
                edad=fields.get("Edad","Sin Edad")
                celular=fields.get("Celular","Sin celular")
                datosEstudiante+=f"  {nombre} - {carrera} - {edad}años - celular:{celular}  "
                nombreObtenido.append({nombre})
            
            print(nombreObtenido)
            resultado.value=datosEstudiante
            
            for datos in nombreObtenido:
                chip=ft.Chip(label=ft.Text(datos))
                nombreBD.controls.append(chip)

            contenedorChips.controls.append(chip)

            
                
        page.update()


    boton=ft.CupertinoFilledButton("Mostrar Estudiantes",on_click=mostrarDatos)
    
    page.add(
        boton,resultado,contenedorChips,
        ft.Column([
            ft.Text("Lista de nombres"),
            nombreBD
        ],expand=True)
    )

ft.app(main)
 