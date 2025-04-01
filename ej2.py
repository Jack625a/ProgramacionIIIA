#Clase Automovil
#PASO 1. definir la clase
class Automovil:
    #Paso 2. definir el constructor
    def __init__(self, motor,marca,modelo,color):
        self.motor=motor
        self.marca=marca
        self.modelo=modelo
        self.color=color

    #Paso 3. Definir las acciones
    def acelerar(self,velocidad):
        print("El auto esta acelerando a ",velocidad)
    
    def frenar(self):
        print("El auto esta frenando")
    

#


#Paso 4. CREAR LOS OBJETOS DE LA CLASE
auto1=Automovil("1800","Toyota",1998,"Azul")
auto2=Automovil("2000","Nissan",2020,"Blanco")

auto1.acelerar(20)
auto2.acelerar(30)
auto1.frenar()
auto2.frenar()