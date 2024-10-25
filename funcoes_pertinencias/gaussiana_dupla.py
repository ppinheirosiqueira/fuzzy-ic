import math
from .generica import funcao_pertinencia

class gaussiana_dupla(funcao_pertinencia):

    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}
        pass

    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções Gaussianas Duplas:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float, sigma1, c1, sigma2, c2):
        gauss1 = math.e**(-((x - c1)**2) / (2 * sigma1**2))
        gauss2 = math.e**(-((x - c2)**2) / (2 * sigma2**2))
        return gauss1 + gauss2
