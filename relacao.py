import numpy as np
import matplotlib.pyplot as plt

def get_valor_norma(funcao:str, a, b, p = 0, gama = 0):
    match funcao:
        case 'Soma Limitada':
            return min(a + b, 1)
        case 'Diferença Limitada':
            return max(a+b - 1, 0)
        case 'Soma Probabilistica':
            return a + b - a*b
        case 'Produto Algébrico':
            return a*b
        case 'Norma T - Lukasiewicz':
            return max(0,(1+p)*(a+b - 1) - p*a*b)
        case 'Norma S - Lukasiewicz':
            return min(1,a+b + p*a*b)
        case 'Norma T - Hamacher':
            return (a*b)/(gama + (1 - gama)*(a+b - a*b))
        case 'Norma S - Hamacher':
            return (a+b - 2*a*b + gama*a*b)/(1 - (1 - gama)*a*b)
        case "Máximo de Zadeh":
            return max(a,b)
        case "Mínimo de Zadeh":
            return min(a,b)
        case "Weber Prod. Drástico":
            if a == 1:
                return b
            if b == 1:
                return a
            return 0
        case "Weber Soma Drástica":
            if a == 0:
                return b
            if b == 0:
                return a
            return 0
        case _:
            print('No match found')

def get_relacao(fuzzyficador_1, fuzzyficador_2, tipo_1:str, funcao_1, tipo_2, funcao_2, norma:str, p=0, gama=0, ax=None):
    x = np.arange(fuzzyficador_1.dominio[0], fuzzyficador_1.dominio[1], 0.1)
    y = np.arange(fuzzyficador_2.dominio[0], fuzzyficador_2.dominio[1], 0.1)

    # Cria uma grade de valores X e Y
    X, Y = np.meshgrid(x, y)

    # Calcula o valor de Z para cada par de (x, y) da grade
    z = []
    for i in x:
        aux = []
        for j in y:
            x_val = i
            y_val = j
            z_valor = get_valor_norma(
                norma,
                fuzzyficador_1.get_pertinencia_especifica([x_val], tipo_1, funcao_1)[0],
                fuzzyficador_2.get_pertinencia_especifica([y_val], tipo_2, funcao_2)[0],
                p,
                gama
            )
            aux.append(z_valor)
        z.append(aux)

    z = np.array(z)  # Converte para array numpy

    # Plota no eixo fornecido ou no padrão
    scatter = ax.scatter(X, Y, c=z, cmap='coolwarm', marker='s', edgecolor='none')
    ax.set_xlabel(f"Domínio do {tipo_1}")
    ax.set_ylabel(f"Domínio do {tipo_2}")
    ax.set_title(f"Relação do {tipo_1} - {funcao_1} com o {tipo_2} - {funcao_2} por {norma}")
    return scatter

def plot_relacoes(fuzzyficador_1, fuzzyficador_2, tipo_1:str, funcao_1, tipo_2, funcao_2, normas:list, p=0, gama=0):
    num_normas = len(normas)
    
    # Determina o número de linhas e colunas para a grade
    num_cols = 2  # Número de colunas desejadas
    num_rows = (num_normas + num_cols - 1) // num_cols  # Número de linhas calculado

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(5 * num_cols, 5 * num_rows))
    
    # Se há apenas uma norma, coloca no formato de lista para manter a consistência
    if num_normas == 1:
        axs = np.array([[axs]])  # Converte para uma matriz 2D

    axs = axs.flatten()  # Achata a matriz de subplots para facilitar a iteração

    for ax, norma in zip(axs, normas):
        scatter = get_relacao(fuzzyficador_1, fuzzyficador_2, tipo_1, funcao_1, tipo_2, funcao_2, norma, p, gama, ax=ax)

    # Remove subplots vazios se houver
    for ax in axs[num_normas:]:
        fig.delaxes(ax)

    # Cria a barra de cor com um parâmetro de localização ajustado
    cbar = fig.colorbar(scatter, ax=axs, orientation='vertical', fraction=0.02, pad=0.04)
    cbar.set_label("Valor entre 0 e 1")

    plt.tight_layout()
    plt.subplots_adjust(right=0.85)  # Ajusta a figura para dar espaço para a barra de cor
    plt.show()

def plot_relacao(fuzzyficador_1, fuzzyficador_2, tipo_1:str, funcao_1, tipo_2, funcao_2, norma, p = 0, gama = 0):
    get_relacao(fuzzyficador_1, fuzzyficador_2, tipo_1, funcao_1, tipo_2, funcao_2, norma, p, gama)
    plt.show()