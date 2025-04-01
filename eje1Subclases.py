#CREAR UNA CLASE PARA ANIMALES
#PASO 1. DEFINIR LA CLASE
class Animal:
    #Paso 2. Definir el constructor
    def __init__(self,tipo,color, tamaño,peso):
        self.tipo=tipo
        self.color=color
        self.tamaño=tamaño
        self.peso=peso
    
    #Paso 3. Acciones de la clase
    def comer(self,comida):
        print("esta comiendo", comida)
    
    def caminar(self):
        print("esta caminando")

#Subclase AnimalesDomesticos
#Paso 1. Definir la subclase
class AnimalesDomesticos(Animal):
    #Paso 2. Definir el contructor
    def __init__(self,tipo,color,tamaño,peso,nombre,edad):
        #Paso 3. Heredar los atrutos de la clase padre
        super().__init__(tipo,color,tamaño,peso)
        #Paso 4. Definir la propiedades de la subclase
        self.nombre=nombre
        self.edad=edad
    #Paso 5. Definir las acciones de la subclase
    def pasear(self,correa):
        if correa==False:
            print(f"{self.nombre} no puede salir")
        else:
            print(f"{self.nombre} esta paseando...") 

#Subclase AnimalesSalvajes
class AnimalesSalvajes(Animal):
    def __init__(self,tipo,color,tamaño,peso,habitad):
        super().__init__(tipo,color,tamaño,peso)
        self.habitad=habitad
    def cazar(self):
        print(f"{self.tipo} esta cazando su presa para comer...")

#Objetos de las subclase

perro=AnimalesDomesticos("Chapi","Blanco",15,8,"Chico",2)
gato=AnimalesDomesticos("Siames","crema",12,8,"Lucas",1)
leon=AnimalesSalvajes("Leon Africano","Dorado",120,100,"Africa")

perro.comer("Carne")
leon.cazar()
leon.comer("Carne")