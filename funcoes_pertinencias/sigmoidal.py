import math
from .generica import funcao_pertinencia

class sigmoidal(funcao_pertinencia):

    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}
        numero_de_divisoes = numero_de_funcoes - 1

        intervalo = diferenca/numero_de_divisoes

        # A inclinação é difícil mensurar
        # Dado que ao contrário da Gaussiana, esta ao subir ficará em 1 para sempre
        # Ou seja, todos os valores altos numa sigmoidal acabam em 1 de pertinência
        # De qualquer forma, vou colocar como atingindo o máximo em meio intervalo
        # Ou seja, é uma inclinação que começa em 0 e vai até 1 em intervalo/2

        inclinacao = 2/intervalo

        for i in range(numero_de_funcoes):
            self.dominios[i] = [inclinacao, intervalo*i]
            
    def get_pertinencias(self,x:float):
        pertinencias = []
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
        return pertinencias

    def get_pertinencia(self,x:float,a,c):
        return 1/(1 + math.e**(-a*(x - c)))
