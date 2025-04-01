#Una clase se define como una class(ClasePadre)
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
    

#Definicion de una Subclase
class Electrico(Automovil):
    #HERENCIA super()
    def __init__(self,motor,marca,modelo,color,bateria):
        super().__init__(motor,marca,modelo,color) #herencia de atrinbutos
        self.bateria=bateria

    #Acciones o metodos
    def cargarBateria(self):
        print("CARGANDO ENERGIA...")

     


#Paso 4. CREAR LOS OBJETOS DE LA CLASE
auto1=Automovil("1800","Toyota",1998,"Azul")
auto2=Automovil("2000","Nissan",2020,"Blanco")

auto1.acelerar(20)
auto2.acelerar(30)
auto1.frenar()
auto2.frenar()


#oBJETO DE LA SUBCLASE
auto3=Electrico("2000","Quantum",2024,"Verde",50)
auto4=Electrico("3000","Tesla",2025,"Plomo",100)
auto3.acelerar(10)
auto3.cargarBateria()
auto4.acelerar(50)
auto4.cargarBateria()