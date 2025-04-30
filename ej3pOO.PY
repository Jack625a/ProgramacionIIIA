#CREAR UN PROGRAMA PARA CAJEROS AUTOMATICOS DONDE UN USUARIO PUEDA 
#RETIRAR, DEPOSITAR Y VER SU SALDO Y CLASIFICAR ENTRE TRES TIPOS DE USUARIOS
#USUARIO NORMAL, USUARIO PREFERENCIAL, USUARIOS VIP
#CLASE CAJERO 
#CLASE USUARIO (nombre,saldo,ci)
#subclase (usuario normal)
#subclase (usuario preferencial)
#subclase (usuario vip)
#Paso 1. Crear la clase padre
class Usuario:
    #Paso 2. definir el constructor
    def __init__(self,nombre,saldo,ci):
        self.nombre=nombre
        self.saldo=saldo
        self.ci=ci
    #Paso 3. Definir las acciones de la clase
    def verSaldo(self):
        print(f"Cuenta: {self.nombre} su saldo actual es: {self.saldo} Bs")

    def depositar(self,monto):
        if monto>0:
            self.saldo=self.saldo+monto
            print(f"Deposito Exitoso saldo actual: {self.saldo} Bs")
        else:
            print("Error monto invalido")
    def retirar(self,monto):
        if monto>self.saldo:
            print("Error saldo insuficiente...")
        else:
            self.saldo=self.saldo-monto
            print(f"Retiro Existoso saldo actual {self.saldo} Bs")


#usuario1=Usuario("Kevin",0,1234567)
#usuario1.verSaldo()
#usuario1.depositar(25)
#usuario1.retirar(20)

#Paso4. Subclases
class UsuarioNormal(Usuario):
    def __init__(self,nombre,saldo,ci):
        #Paso5. Realizar la herencia de los atributos
        #super()
        super().__init__(nombre,saldo,ci)
        #Variable nativa
        self.limiteRetiro=1000
    
    #Paso 6. Polimorfismo (heredar acciones y modificarlos)
    def retirar(self,monto):
        if monto>self.limiteRetiro:
            print("Error no puede retirar mas de 1000bs en su tipo de cuenta...")
        elif monto<=self.saldo:
            self.saldo=self.saldo-monto
            print(f"Retiro Normal se realizo correctamente: saldo actual {self.saldo}")
        else:
            print("Error saldo insuficiente....")


usuario1=UsuarioNormal("Kevin",4500,1234567)
usuario1.retirar(1500)

#Subclase2
class UsuarioPreferencial(Usuario):
    def __init__(self,nombre,saldo,ci):
        super(). __init__(nombre,saldo,ci)
        #variables o parametros nativos 
        self.limite=5000
        self.promociones=True

    #Acciones de la clase
    def retirar(self,monto):
        if monto>self.limite:
            print(f"Superaste tu limite de retiros de 5000bs...")
        elif monto<=self.saldo:
            self.saldo=self.saldo-monto
            print(f"Retiro Preferencial realizado correctamente: saldo actual {self.saldo}Bs")
        else:
            print("Error saldo insuficiente")
    def promocion(self):
        if self.promociones:
            print("Promociones vigentes...")

usuarioP=UsuarioPreferencial("Juan",5500,4567891)
usuarioP.promocion()
usuarioP.retirar(4550)

class UsuarioVip(Usuario):
    def __init__(self,nombre,saldo,ci):
        super(). __init__(nombre,saldo,ci)
        self.limite="Ilimitado"
        self.promociones=True
        self.accesoPersonalizado=True
    
    def retirar(self,monto):
        if self.limite=="Ilimitado":
            if monto<=self.saldo:
                self.saldo=self.saldo-monto
                print(f"Retiro Vip se realizo correctamente saldo actual es {self.saldo}Bs ")
            else:
                print("Saldo insuficiente")

usuarioV=UsuarioVip("ana",78000,4561257)
usuarioV.retirar(20000)



