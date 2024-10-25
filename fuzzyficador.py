import funcoes_pertinencias as fp

class fuzzyficador:

    def __init__(self, x1:float, x2:float,numero_de_funcoes:int):
        if x1 == x2:
            raise ValueError("Erro: Não é possível ter dois limites iguais")
        
        minimo = min(x1,x2)
        maximo = max(x1,x2)

        diferenca = maximo - minimo

        self.funcoes = {
            "Triangular não complementar": fp.triangular(diferenca, numero_de_funcoes),
            "Triangular complementar": fp.triangular_complementar(diferenca, minimo, maximo, numero_de_funcoes),
            "Trapezoidal": fp.trapezoidal(diferenca, minimo, maximo, numero_de_funcoes),
            "Gaussiana": fp.gaussiana(diferenca, numero_de_funcoes),
            "Sigmoidal": fp.sigmoidal(diferenca, numero_de_funcoes),
            "Sino Generalizada": fp.sino_generalizada(diferenca, numero_de_funcoes),
            "Z Shaped": fp.z_shaped(diferenca, numero_de_funcoes),
            "S Shaped": fp.s_shaped(diferenca, numero_de_funcoes),
            "Cauchy": fp.cauchy(diferenca,numero_de_funcoes),
            "Gaussiana Dupla": fp.gaussiana_dupla(diferenca,numero_de_funcoes),
            "Exponencial": fp.exponencial(diferenca,numero_de_funcoes),
            "Pi Shaped": fp.pi_shaped(diferenca,minimo,maximo,numero_de_funcoes)
        }
    
    def get_pertinencia(self,x:float):
        for item in self.funcoes:
            self.funcoes[item].get_pertinencias(x)