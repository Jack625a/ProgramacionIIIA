print("Codigo en Python")
#SINTAXIS BASICA DE PYTHON
#VARIABLES - TIPOS DE DATOS
#tipos de datos (numericos, cadena caracteres, booleanos)
numero=15
numero2= 15.2
nombre="Kevin"
nombre2='Juan'
numero3='5'
encender=True #False
#Tipos de Datos Complejos
#Listas [], Tuplas (), Diccionarios {}
colores=["rojo","verde","azul"]
lista=[455,12.5,"abc",True]
#Acciones para una lista
print(lista)
#Insercion de datos
lista.append("Hola")
print(lista)
#Insert
lista.insert(1,"hola2")
print(lista)
lista.insert(1,"hola3")
print(lista)
#mostrar el ultimo elemento de una lista
print(lista[-1])
#longitud de una lista count
#len (longitud de elemento)
print(len(lista))

#TUPLAS
numeros4=(45,68,636,6,5,3)

print(numeros4[0])

#Diccionarios
diccionario={
    "nombre":"Kevin",
    "celular":654023654,
    "notificacion":True,
    "carrera":"Ingenieria de Sistemas"
}
print(diccionario["nombre"])

print(diccionario.get("profesion","Ingeniero"))

diccionario["carrera"]="aavvas"
print(diccionario)

#bucles
#Bucles iterativos fo
for iterador in range(11):
    print(iterador)

#Eje1. Mostra la tabla del 8 con un bucle for

for a in range(11):
    print(f"{a}x8={a*8}")

#Mostrar la tabla de multiplicar 
# de cualquier numero ingresado por teclado
valorTabla=int(input("que tabla de mutiplicar deseea?: "))
for a in range(11):
    print(f"{a}x{valorTabla}={a*valorTabla}")
#CVALORES POR TECLAS input
nombreCompleto=input("Ingrese su nombre: ")

#Funciones def
#Funciones sin parametros
def saludar():
    print("Hola bienvenidos")

#Mostrar una funcion
saludar()
#funciones con parametros
def sumar(a,b):
    return a+b
print(sumar(5,8))