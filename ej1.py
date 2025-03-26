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
    
    def respirar(self):
        print("esta respirando")

conejo=Animal("mamifero","blanco",50,2.5)
araña=Animal("aracnido","negro",8,0.5)
perro=Animal("mamifero","cafe",25,8)

perro.comer("Carne")
conejo.respirar()
araña.comer("mosca")
        
