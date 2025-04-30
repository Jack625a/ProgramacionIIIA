class padre:
    def __init__(self,x):
        self.x=x
        self.salario=2500
    def calcularSalario(self):
        self.salario=2500

class E1(padre):
    def __init__(self):

    def calcularSalario(self,bono):
        self.salario=self.salario+bono

class tm(padre):

    def calcularSalario(self,horas):
        self.salario=(self.salario/8)*horas

class fre(padre):
    def calcularSalario(self,numeroProyectos):
        self.salario=self.salario*numeroProyectos
    
        
        