#crear una funcion para una calculadora simple
def calculadora(x,y):
    while True:
        print("Bienvenido a la calculadora")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion=input("Ingrese la operacion que desea realizar: ")
        if opcion=="1":
            print(f"{x}+{y}={x+y}")
            return x+y
            
        elif opcion=="2":
            print(f"{x}-{y}={x-y}")
            return x-y
        elif opcion=="3":
            print(f"{x}x{y}={x*y}")
            return x*y
        elif opcion=="4":
            print(f"{x}/{y}={x/y}")
            return x/y
        elif opcion==5:
            print("Gracias por utilizar la calculadora...")
            break
        else: 
            print("Error operacion invalida...")

calculadora(7,5)
calculadora(11,6)