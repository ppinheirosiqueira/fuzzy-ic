import numpy as np
import matplotlib.pyplot as plt

def composicao_max_min(linha, coluna):
    return np.max(np.minimum(linha, coluna))

def composicao_min_max(linha, coluna):
    return np.min(np.maximum(linha, coluna))

def composicao_max_prod(linha, coluna):
    return np.max(linha * coluna)

def calcular_composicao(matriz_1, matriz_2, composicao):
    if matriz_1.shape[1] != matriz_2.shape[0]:
        raise ValueError("Número de colunas da matriz 1 deve ser igual ao número de linhas da matriz 2.")

    resultado = np.zeros((matriz_1.shape[0], matriz_2.shape[1]))

    for i in range(matriz_1.shape[0]):
        for j in range(matriz_2.shape[1]):
            linha = matriz_1[i, :]
            coluna = matriz_2[:, j]

            if composicao == "max-min":
                resultado[i, j] = composicao_max_min(linha, coluna)
            elif composicao == "min-max":
                resultado[i, j] = composicao_min_max(linha, coluna)
            elif composicao == "max-prod":
                resultado[i, j] = composicao_max_prod(linha, coluna)
            else:
                raise ValueError("Tipo de composição inválido.")

    return resultado

def plotar_composicoes(matriz_1,matriz_2,nome_matriz_1,nome_matriz_2):
    comp_max_min = calcular_composicao(matriz_1, matriz_2, "max-min")
    comp_min_max = calcular_composicao(matriz_1, matriz_2, "min-max")
    comp_max_prod = calcular_composicao(matriz_1, matriz_2, "max-prod")
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].imshow(comp_max_min, cmap="coolwarm", interpolation="nearest", origin="lower")
    axs[0].set_title("Composição Max-Min")
    axs[0].set_xlabel("Conjunto B")
    axs[0].set_ylabel("Conjunto A")

    axs[1].imshow(comp_min_max, cmap="coolwarm", interpolation="nearest", origin="lower")
    axs[1].set_title("Composição Min-Max")
    axs[1].set_xlabel("Conjunto B")

    axs[2].imshow(comp_max_prod, cmap="coolwarm", interpolation="nearest", origin="lower")
    axs[2].set_title("Composição Max-Prod")
    axs[2].set_xlabel("Conjunto B")

    plt.colorbar(axs[0].imshow(comp_max_min, cmap="coolwarm", interpolation="nearest"), ax=axs, orientation='horizontal')

    fig.text(0.5, 0.01, f"Conjunto A: {nome_matriz_1} | Conjunto B: {nome_matriz_2}", ha='center', fontsize=12)

    plt.show()