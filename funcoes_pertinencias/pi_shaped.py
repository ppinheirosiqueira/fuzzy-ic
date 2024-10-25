from .generica import funcao_pertinencia

class pi_shaped(funcao_pertinencia):
    
    def __init__(self, diferenca:float,minimo:float,maximo:float,numero_de_funcoes:int):
        self.dominios = {}

        numero_de_divisoes = 2*numero_de_funcoes - 1

        intervalo = diferenca/numero_de_divisoes

        for i in range(numero_de_funcoes):
            if i == 0:
                self.dominios[i] = [minimo, minimo, intervalo, intervalo*2]
            elif i == numero_de_funcoes - 1:
                self.dominios[i] = [maximo - intervalo*2, maximo - intervalo, maximo, maximo]
            else:
                self.dominios[i] = [intervalo*i, intervalo*(i + 1), intervalo*(i+2), intervalo*(i+3)]

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

