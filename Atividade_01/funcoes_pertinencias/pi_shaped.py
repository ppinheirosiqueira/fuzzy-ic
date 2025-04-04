from .generica import funcao_pertinencia

class pi_shaped(funcao_pertinencia):
    
    def __init__(self, diferenca:float,minimo:float,maximo:float,numero_de_funcoes:int):
        self.dominios = {}

        numero_de_divisoes = numero_de_funcoes

        intervalo = diferenca/numero_de_divisoes

        for i in range(numero_de_funcoes):
            self.dominios[i] = [intervalo*(i - 1), intervalo*(i), intervalo*(i+1), intervalo*(i+2)]

    def get_pertinencias(self,x:float):
        pertinencias = []
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
        return pertinencias

    def get_pertinencia(self,x:float,a,b,c,d):
        if x <= a or x >= d:
            return 0.0
        
        if x <= (a+b)/2:
            return 2*((x-a)/(b-a))**2

        if x <= b:
            return 1 - 2*((x-b)/(b-a))**2

        if x <= c:
            return 1.0
        
        if x <= (c+d)/2:
            return 1 - 2*((x-c)/(d-c))**2
        
        return 2*((x-d)/(d-c))**2

