#Clase padre animales Domesticos
#Paso 1. definir la clase padre
class AnimalesDomesticos:
    #Paso 2. Definir constructor
    def __init__(self,nombre,color,tipo,tamaño,peso):
        self.nombre=nombre
        self.color=color
        self.tipo=tipo
        self.tamaño=tamaño
        self.peso=peso
    #Paso 3. Definir las acciones de la clase
    def comer(self):
        print(f"{self.nombre} esta comiendo")
    def pasear(self):
        print(f"{self.nombre} esta paseando")

#Subclases
#Paso 1. Definir la subclase class(clasePadre)
class Perro(AnimalesDomesticos):
    #Paso 2. Definir el constructor
    def __init__(self,nombre,color,tipo,tamaño,peso,raza):
        #Paso 3. Heredar los atributos de la clase padre super()
        super().__init__(nombre,color,tipo,tamaño,peso)
        #Paso 4. Definir las propiedades de la subclase
        self.raza=raza
    #PaSO 5. Definir las acciones de la subclase
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

    def comer(self,comida):
        #super().comer(comida)
        print(f"{self.nombre} esta comiendo {comida}") 



perro1=Perro("Rex","Cafe","Domestico",50,12,"Criollo")
gato=AnimalesDomesticos("Luna","Blanco","Domestico",12,7)
gato.comer()
perro1.comer("carne con arroz")