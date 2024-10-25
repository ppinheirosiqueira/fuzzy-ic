from .generica import funcao_pertinencia

class cauchy(funcao_pertinencia):  

    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}

        numero_de_divisoes = numero_de_funcoes - 1

        intervalo = diferenca/numero_de_divisoes

        met_int = 0.5*intervalo

        for i in range(numero_de_funcoes):
            self.dominios[i] = [met_int,intervalo*i]

    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções Cauchy:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float,a,c):
        return 1/(1 + ((x-c)/a)**2)

