import math
from .generica import funcao_pertinencia

class gaussiana(funcao_pertinencia):

    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}
        numero_de_divisoes = numero_de_funcoes - 1

        intervalo = diferenca/numero_de_divisoes

        # O desvio padrão será uma loucura de calcular
        # Imaginando que os intervalos são de tamanho X
        # Quero que em X/2, ou seja, bem no meio das duas primeiras curvas, a soma das pertinências seja próxima de 1
        # Pela fórmula da gaussiana isso da que o desvio padrão é igual a
        # σ= x / 2sqr(2ln(2))

        sigma = intervalo/(2*math.sqrt(2*math.log(2,math.e)))

        for i in range(numero_de_funcoes):
            self.dominios[i] = [intervalo*i, sigma]

    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções Gaussianas:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float,c,sigma):
        return math.e**((-(x-c)**2)/(2*sigma**2))
