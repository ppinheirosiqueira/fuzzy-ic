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

    def get_grafico_uniao(self, titulo:str, dominio:list, zadeh:bool = False):
        x_values = np.arange(dominio[0], dominio[1], 0.1)

        figura  = plt.figure()
        if zadeh:
            plt.title(f"Máximo de Zadeh - {titulo}")
        else:
            plt.title(f"União - {titulo}")
        plt.xlabel('Domínio')
        plt.ylabel('Pertinência')
        
        y_values = self.get_y_values_normas("União",x_values)

        plt.plot(x_values, y_values, label="União", linewidth=2)

        plt.legend()
        plt.grid(True)
        plt.ylim(0, 1.1)

        return figura
    
    def plot_intersecao(self, titulo:str, dominio:list):
        self.get_grafico_intersecao(titulo, dominio)
        plt.show()

    def get_grafico_intersecao(self, titulo:str, dominio:list, zadeh:bool = False):
        x_values = np.arange(dominio[0], dominio[1], 0.1)

        figura  = plt.figure()
        if zadeh:
            plt.title(f"Mínimo de Zadeh - {titulo}")
        else:
            plt.title(f"Interseção - {titulo}")
        plt.xlabel('Domínio')
        plt.ylabel('Pertinência')
        
        y_values = self.get_y_values_normas("Interseção",x_values)


        plt.plot(x_values, y_values, label="Interseção", linewidth=2)

        plt.legend()
        plt.grid(True)
        plt.ylim(0, 1.1)

        return figura
    
    def plot_normas_duais(self, titulo:str, dominio:list):
        self.plot_t_normas(titulo, dominio)
        self.plot_s_normas(titulo, dominio)

    def get_t_normas(self, titulo:str, dominio:list, p:float, gama: float):
        # São as minimas
        figuras = [
            self.get_padrao_normas("Mínimo de Zadeh", dominio),
            self.get_padrao_normas("Produto Algébrico", dominio),
            self.get_padrao_normas("Norma T - Lukasiewicz", dominio, p),
            self.get_padrao_normas("Norma T - Hamacher", dominio, 0, gama),
            self.get_padrao_normas("Diferença Limitada", dominio),
            self.get_padrao_normas("Weber Prod. Drástico", dominio)
        ]
        
        fig, axs = plt.subplots(3, 2, figsize=(10, 8))
        fig.suptitle(f"T-Normas {titulo}", fontsize=16)

        for ax, figura in zip(axs.ravel(), figuras):
            for line in figura.gca().get_lines():
                ax.plot(line.get_xdata(), line.get_ydata(), label=line.get_label())
            
            ax.set_title(figura._suptitle.get_text() if figura._suptitle else titulo)
            ax.legend()
            ax.grid(True)
        
        plt.tight_layout()

    def plot_t_normas(self, titulo:str, dominio:list, p:float, gama: float):
        figura = self.get_t_normas(titulo, dominio, p, gama)
        plt.show()

    def get_s_normas(self, titulo:str, dominio:list, p:float, gama: float):
        # São as minimas
        figuras = [
            self.get_padrao_normas("Máximo de Zadeh", dominio),
            self.get_padrao_normas("Soma Probabilistica", dominio),
            self.get_padrao_normas("Norma S - Lukasiewicz", dominio, p),
            self.get_padrao_normas("Norma S - Hamacher", dominio, 0, gama),
            self.get_padrao_normas("Soma Limitada", dominio),
            self.get_padrao_normas("Weber Soma Drástica", dominio)
        ]
        
        fig, axs = plt.subplots(3, 2, figsize=(10, 8))
        fig.suptitle(f"S-Normas {titulo}", fontsize=16)

        for ax, figura in zip(axs.ravel(), figuras):
            for line in figura.gca().get_lines():
                ax.plot(line.get_xdata(), line.get_ydata(), label=line.get_label())
            
            ax.set_title(figura._suptitle.get_text() if figura._suptitle else titulo)
            ax.legend()
            ax.grid(True)
        
        plt.tight_layout()

    def plot_s_normas(self, titulo:str, dominio:list, p, gama):
        # São as máximas
        figura = self.get_s_normas(titulo, dominio, p, gama)
        plt.show()

    def get_padrao_normas(self, tipo:str, dominio:list, p = 0, gama = 0):
        x_values = np.arange(dominio[0], dominio[1], 0.1)
        figura  = plt.figure()
        plt.xlabel('Domínio')
        plt.ylabel('Pertinência')
        plt.suptitle(f"{tipo}")
        y_values = self.get_y_values_normas(tipo,x_values, p, gama)
        plt.plot(x_values, y_values, linewidth=2)
        plt.close(figura) 
        return figura

    def get_y_values_normas(self, funcao:str, x_values, p = 0, gama = 0):
        y_values = []

        match funcao:
            case 'Soma Limitada':
                for x in x_values:
                    aux_soma = 0
                    for funcao, params in self.dominios.items():
                        aux_soma += self.get_pertinencia(x, *params)
                    
                    y_values.append(min(aux_soma, 1))
            case 'Diferença Limitada':
                for x in x_values:
                    aux_soma = 0
                    for funcao, params in self.dominios.items():
                        aux_soma += self.get_pertinencia(x, *params)
                    
                    y_values.append(max(aux_soma - 1, 0))
            case 'Soma Probabilistica':
                for x in x_values:
                    aux_soma = 0
                    aux_prod = 1
                    for funcao, params in self.dominios.items():
                        aux_pertinencia = self.get_pertinencia(x, *params)
                        aux_soma += aux_soma
                        aux_prod *= aux_pertinencia
                    
                    y_values.append(aux_soma - aux_prod)
            case 'Produto Algébrico':
                for x in x_values:
                    aux = 1
                    for funcao, params in self.dominios.items():
                        aux *= self.get_pertinencia(x, *params)
                    
                    y_values.append(aux)
            case 'Interseção':
                for x in x_values:
                    aux = []
                    for funcao, params in self.dominios.items():
                        aux.append(self.get_pertinencia(x, *params))
                    
                    y_values.append(min(aux))
            case 'União':
                for x in x_values:
                    aux = []
                    for funcao, params in self.dominios.items():
                        aux.append(self.get_pertinencia(x, *params))
                    
                    y_values.append(max(aux))
            case 'Norma T - Lukasiewicz':
                for x in x_values:
                    aux_soma = 0
                    aux_prod = 1
                    for funcao, params in self.dominios.items():
                        aux_pertinencia = self.get_pertinencia(x, *params)
                        aux_soma += aux_pertinencia
                        aux_prod *= aux_pertinencia
                    
                    y_values.append(max(0,(1+p)*(aux_soma - 1) - p*aux_prod))
            case 'Norma S - Lukasiewicz':
                for x in x_values:
                    aux_soma = 0
                    aux_prod = 1
                    for funcao, params in self.dominios.items():
                        aux_pertinencia = self.get_pertinencia(x, *params)
                        aux_soma += aux_pertinencia
                        aux_prod *= aux_pertinencia
                    
                    y_values.append(min(1,aux_soma + p*aux_prod))
            case 'Norma T - Hamacher':
                for x in x_values:
                    aux_soma = 0
                    aux_prod = 1
                    for funcao, params in self.dominios.items():
                        aux_pertinencia = self.get_pertinencia(x, *params)
                        aux_soma += aux_soma
                        aux_prod *= aux_pertinencia
                    
                    y_values.append(aux_prod/(gama + (1 - gama)*(aux_soma - aux_prod)))
            case 'Norma S - Hamacher':
                for x in x_values:
                    aux_soma = 0
                    aux_prod = 1
                    for funcao, params in self.dominios.items():
                        aux_pertinencia = self.get_pertinencia(x, *params)
                        aux_soma += aux_soma
                        aux_prod *= aux_pertinencia
                    
                    y_values.append((aux_soma - 2*aux_prod + gama*aux_prod)/(1 - (1 - gama)*aux_prod))
            case "Máximo de Zadeh":
                y_values = self.get_y_values_normas("União", x_values)
            case "Mínimo de Zadeh":
                y_values = self.get_y_values_normas("Interseção", x_values)
            case "Weber Prod. Drástico":
                for x in x_values:
                    aux = []
                    for funcao, params in self.dominios.items():
                        aux.append(self.get_pertinencia(x, *params))
                    
                    y_values.append(self.verificar_valores_produto(aux))
            case "Weber Soma Drástica":
                for x in x_values:
                    aux = []
                    for funcao, params in self.dominios.items():
                        aux.append(self.get_pertinencia(x, *params))
                    
                    y_values.append(self.verificar_valores_soma(aux))
            case _:
                print('No match found')
        return y_values
    
    def verificar_valores_produto(self, x):
        for i in x:
            if all(val == 1 for val in x if val != i):
                return i
        return 0
    
    def verificar_valores_soma(self, x):
        for i in x:
            if all(val == 0 for val in x if val != i):
                return i
        return 1
    