from .generica import funcao_pertinencia

class s_shaped(funcao_pertinencia):
    
    def __init__(self, diferenca:float,numero_de_funcoes:int):
        self.dominios = {}

        numero_de_divisoes = numero_de_funcoes + 1

        intervalo = diferenca/numero_de_divisoes

        for i in range(numero_de_funcoes):
            self.dominios[i] = [intervalo*(i+1),intervalo*(i+2)]

    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções S Shaped:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float,a,b):
        if x <= a:
            return 0.0
        
        b_menos_a = b - a

        if x <= (a + b)/2:
            return 2*((x-a)/b_menos_a)**2    
        
        if x <= b:
            return 1 - 2*((b-x)/(b_menos_a))**2

        return 1.0

