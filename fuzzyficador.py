import funcoes_pertinencias as fp
import matplotlib.pyplot as plt

class fuzzyficador:

    def __init__(self, x1:float, x2:float,numero_de_funcoes:int):
        if x1 == x2:
            raise ValueError("Erro: Não é possível ter dois limites iguais")
        
        minimo = min(x1,x2)
        maximo = max(x1,x2)

        diferenca = maximo - minimo

        self.dominio = [minimo, maximo]

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
    
    def get_pertinencia(self,lista_valores:list):
        pertinencias = {}
        for valor in lista_valores:
            pertinencias[valor] = {}
            for item in self.funcoes:
                pertinencias[valor][item] = self.funcoes[item].get_pertinencias(valor)
        
        return pertinencias
    
    def plot_grafico(self,tipo:str):
        self.funcoes[tipo].plot_grafico(tipo, self.dominio)

    def plot_graficos(self, tipos:list):
        figuras = []
        for chave in tipos:
            figuras.append(self.funcoes[chave].get_grafico(chave, self.dominio))
        plt.show()

    def plot_complemento(self,tipo:str):
        self.funcoes[tipo].plot_complemento(tipo, self.dominio)

    def plot_complementos(self, tipos:list):
        figuras = []
        for chave in tipos:
            figuras.append(self.funcoes[chave].get_grafico_complemento(chave, self.dominio))
        plt.show()

    def plot_uniao(self,tipo:str):
        self.funcoes[tipo].plot_uniao(tipo, self.dominio)

    def plot_unioes(self, tipos:list):
        figuras = []
        for chave in tipos:
            figuras.append(self.funcoes[chave].get_grafico_uniao(chave, self.dominio))
        plt.show()

    def plot_intersecao(self,tipo:str):
        self.funcoes[tipo].plot_intersecao(tipo, self.dominio)

    def plot_intersecoes(self, tipos:list):
        figuras = []
        for chave in tipos:
            figuras.append(self.funcoes[chave].get_grafico_intersecao(chave, self.dominio))
        plt.show()
