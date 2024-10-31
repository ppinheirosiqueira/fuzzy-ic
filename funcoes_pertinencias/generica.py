import matplotlib.pyplot as plt
import numpy as np

class funcao_pertinencia:

    def plot_grafico(self, titulo:str, dominio:list):
        self.get_grafico(titulo, dominio)
        plt.show()

    def get_grafico(self, titulo:str, dominio:list):
        x_values = np.arange(dominio[0], dominio[1], 0.1)

        figura  = plt.figure()
        plt.title(titulo)
        plt.xlabel('Domínio')
        plt.ylabel('Pertinência')
        
        for funcao, params in self.dominios.items():
            y_values = [self.get_pertinencia(x, *params) for x in x_values]
            
            plt.plot(x_values, y_values, label=funcao, linewidth=2)

        plt.legend()
        plt.grid(True)
        plt.ylim(0, 1.1)

        return figura
    
    def plot_complemento(self, titulo:str, dominio:list):
        self.get_grafico_complemento(titulo, dominio)
        plt.show()

    def get_grafico_complemento(self, titulo:str, dominio:list):
        x_values = np.arange(dominio[0], dominio[1], 0.1)

        figura  = plt.figure()
        plt.title(f"Complemento - {titulo}")
        plt.xlabel('Domínio')
        plt.ylabel('Pertinência')
        
        for funcao, params in self.dominios.items():
            y_aux = [self.get_pertinencia(x, *params) for x in x_values]
            y_values = [1 - y for y in y_aux]

            plt.plot(x_values, y_values, label=funcao, linewidth=2)

        plt.legend()
        plt.grid(True)
        plt.ylim(0, 1.1)

        return figura
    
    def plot_uniao(self, titulo:str, dominio:list):
        self.get_grafico_uniao(titulo, dominio)
        plt.show()

    def get_grafico_uniao(self, titulo:str, dominio:list):
        x_values = np.arange(dominio[0], dominio[1], 0.1)

        figura  = plt.figure()
        plt.title(f"União - {titulo}")
        plt.xlabel('Domínio')
        plt.ylabel('Pertinência')
        
        y_values = []

        for x in x_values:
            aux = []
            for funcao, params in self.dominios.items():
                aux.append(self.get_pertinencia(x, *params))
            
            y_values.append(max(aux))

        plt.plot(x_values, y_values, label=funcao, linewidth=2)

        plt.legend()
        plt.grid(True)
        plt.ylim(0, 1.1)

        return figura
    
    def plot_intersecao(self, titulo:str, dominio:list):
        self.get_grafico_intersecao(titulo, dominio)
        plt.show()

    def get_grafico_intersecao(self, titulo:str, dominio:list):
        x_values = np.arange(dominio[0], dominio[1], 0.1)

        figura  = plt.figure()
        plt.title(f"Interseção - {titulo}")
        plt.xlabel('Domínio')
        plt.ylabel('Pertinência')
        
        y_values = []

        for x in x_values:
            aux = []
            for funcao, params in self.dominios.items():
                aux.append(self.get_pertinencia(x, *params))
            
            y_values.append(min(aux))

        plt.plot(x_values, y_values, label=funcao, linewidth=2)

        plt.legend()
        plt.grid(True)
        plt.ylim(0, 1.1)

        return figura