from .generica import funcao_pertinencia

class sino_generalizada(funcao_pertinencia):

    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}
        numero_de_divisoes = numero_de_funcoes - 1

        intervalo =  diferenca/numero_de_divisoes

        # Como é arbitrário o valor da largura e da suavidade
        # Largura vou colocar como 1/4 do intervalo
        # Suavidade vou colocar como 1/2 do intervalo

        met_int = 0.5*intervalo
        um_quarto_int = 0.25*intervalo

        for i in range(numero_de_funcoes):
            self.dominios[i] = [um_quarto_int,met_int,intervalo*i]

    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções Sino Generalizada:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float,a,b,c):
        return  1/(1 + abs((x-c)/a)**(2*b))

