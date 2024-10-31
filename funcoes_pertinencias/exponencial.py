import math
from .generica import funcao_pertinencia

class exponencial(funcao_pertinencia):
    
    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}

        numero_de_divisoes = numero_de_funcoes - 1

        intervalo = diferenca/numero_de_divisoes
        met_int = 0.5*intervalo

        for i in range(numero_de_funcoes):
            self.dominios[i] = [met_int,intervalo*i]

    def get_pertinencias(self,x:float):
        pertinencias = []
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
        return pertinencias

    def get_pertinencia(self,x:float,a,c):
        return math.e**(-abs((x - c) / a))

