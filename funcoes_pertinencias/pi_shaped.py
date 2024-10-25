from .generica import funcao_pertinencia

class pi_shaped(funcao_pertinencia):
    
    def __init__(self, limites:list,numero_de_funcoes:int):
        self.dominios = {}

        pass

    def get_pertinencias(self,x:float):
        pertinencias = []
        print("Nas funções Pi Shaped:")
        for funcao in self.dominios.keys():
            pertinencias.append(self.get_pertinencia(x,*self.dominios[funcao]))
            print(f"O valor {x} tem pertinência {pertinencias[-1]:.2f} no dominio {self.print_dominio(self.dominios[funcao])}")
        print('\n')
        return pertinencias

    def get_pertinencia(self,x:float,a,b,c,d):
        if x <= a or x >= d:
            return 0.0
        
        if x <= (a+b)/2:
            return 2*((x-a)/(b-a))**2

        if x <= b:
            return 1 - 2*((x-b)/(b-a))**2

        if x <= c:
            return 1.0
        
        if x <= (c+d)/2:
            return 1 - 2*((x-c)/(d-c))**2
        
        return 2*((x-d)/(d-c))**2

