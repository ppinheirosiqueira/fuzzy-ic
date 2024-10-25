import math

class exponencial:
    
    def __init__(self, limites:list,numero_de_funcoes:int):
        self.dominios = {}

        pass

    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções Exponenciais:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float,a,c):
        return math.e**(-abs((x - c) / a))

