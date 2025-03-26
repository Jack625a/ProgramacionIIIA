#Elemento de la programacion orientada a objetos
#CLASES 
#PROPIEDADES O ATRIBUTOS
#METODOS O ACCIONES
#OBJETOS 
#CLASE ANIMAL
#PROPIEDADES O ATRIBUTOS
#numeroPatas, edad, especie, color,tamaño, tipoPiel
#acciones de cualquier animal
#comer(), dormir(), reproducirse()

#CLASE class
#propiedades self
#Metodo o acciones def 
#PASO 1. DEFINIR LA CLASE
class Persona: #Nota: la primera letra de la clase va con mayuscula
    #PASO 2. DEFINIR EL CONSTRUCTOR
    def __init__(self,nombre,edad,ci):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
    
    #PASO 3. DEFINIR LAS ACCIONES DE LA CLASE
    def comer(self,comida):
        print(f"{self.nombre} Esta comiendo {comida}")
    
    def dormir(self):
        print(f"{self.nombre}  esta durmiendo ")

    def caminar(self):
        print(f"{self.nombre}  esta caminando...")

#Paso 4. Crear los objetos de la clase
persona1=Persona("Kevin",28,12345687)
persona2=Persona("Ana",25,745122)
persona3=Persona("Jose",21,4565212)

#Paso 5. Probar las acciones de la clase
persona1.comer("Pan")
persona2.dormir()
persona3.caminar()