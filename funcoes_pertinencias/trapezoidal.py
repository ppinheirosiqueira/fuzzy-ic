from .generica import funcao_pertinencia

class trapezoidal(funcao_pertinencia):

    def __init__(self, diferenca:float,minimo:float,maximo:float, numero_de_funcoes:int):
        self.dominios = {}

        numero_de_divisoes = 2*numero_de_funcoes - 1

        intervalo = diferenca/numero_de_divisoes

        for i in range(numero_de_funcoes):
            self.dominios[i] = [intervalo*i, intervalo*(i + 1), intervalo*(i+2), intervalo*(i+3)]

    def get_pertinencias(self,x:float):
        pertinencias = []
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
        return pertinencias

    def get_pertinencia(self,x:float,a,b,c,d):
        if x <= a or x >= d:
            return 0.0

        if x <= b:
            return (x - a) / (b - a)
        
        if x <= c:
            return 1.0

        return (d - x) / (d - c)