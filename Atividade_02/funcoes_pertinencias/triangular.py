from .generica import funcao_pertinencia

class triangular(funcao_pertinencia):

    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}

        numero_de_divisoes = numero_de_funcoes + 1

        intervalo = diferenca/numero_de_divisoes

        for i in range(numero_de_funcoes):
            self.dominios[i] = [intervalo*i, intervalo*(i+1), intervalo*(i+2)]

    def get_pertinencias(self,x:float):
        pertinencias = []
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
        return pertinencias

    def get_pertinencia(self,x:float,a,b,c):
        if x <= a or x >= c:
            return 0.0

        if x <= b:
            return (x - a) / (b - a)
        
        return (c - x) / (c - b)