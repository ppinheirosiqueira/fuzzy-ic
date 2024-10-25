import math
from .generica import funcao_pertinencia

class gaussiana_dupla(funcao_pertinencia):

    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}
        numero_de_divisoes = numero_de_funcoes - 1

        intervalo = diferenca/numero_de_divisoes
        met_int = 0.5*intervalo
        sigma = intervalo/(2*math.sqrt(2*math.log(2,math.e)))

        for i in range(numero_de_funcoes):
            centro = intervalo*i
            self.dominios[i] = [sigma, centro - met_int, sigma, centro + met_int]


    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções Gaussianas Duplas:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float, sigma1, c1, sigma2, c2):
        gauss1 = 0.5*math.e**(-((x - c1)**2) / (2 * sigma1**2))
        gauss2 = 0.5*math.e**(-((x - c2)**2) / (2 * sigma2**2))
        return gauss1 + gauss2
