import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import math
import funcoes_pertinencias as fp

def calcular_z(x,funcoes_pertinencia,vetor_funcoes_z,tipo_funcao):
    z = []
    for ponto in x:
        somatorio_cima = 0
        somatorio_baixo = 0
        for i in range(len(funcoes_pertinencia)):
            pertinencia_ponto = tipo_funcao.get_pertinencia(None, ponto, *funcoes_pertinencia[i])
            somatorio_baixo += pertinencia_ponto
            somatorio_cima += pertinencia_ponto*(vetor_funcoes_z[i][0]*ponto + vetor_funcoes_z[i][1])
        z.append(somatorio_cima/somatorio_baixo if somatorio_baixo != 0 else 1)
    return z

def calcular_erro(z, f_x, erros):
    erro = 0
    for i in range(len(f_x)):
        erro += (f_x[i] - z[i])**2

    erro = erro/len(f_x)
    erro = erro**(1/2)
    erros.append(erro)

def att_funcoes(vetor_funcoes_z, i, j, multiplicador, ganho, geracao_atual):
    vetor_funcoes_z[i][j] += multiplicador*ganho
    return geracao_atual + 1

def check_erro(menor_erro, geracao_atual, erros, z):
    if erros[-1] < menor_erro:
        menor_z = copy.deepcopy(z)
        menor_erro = erros[-1]
        melhor_ger = geracao_atual
        return menor_z, menor_erro, melhor_ger
    
def att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger,tipo_funcao):
    geracao_atual = att_funcoes(vetor_funcoes_z, i, j, multiplicador, ganho, geracao_atual)
    z = calcular_z(x, funcoes_pertinencia, vetor_funcoes_z, tipo_funcao)
    calcular_erro(z, f_x, erros)
    resultado = check_erro(menor_erro, geracao_atual, erros, z)
    if resultado is not None:
        menor_z, menor_erro, melhor_ger = resultado
    return geracao_atual, menor_z, menor_erro, melhor_ger

def aproximar(x, f_x, numero_funcoes, erro_minimo, tipo_funcao):
    funcoes = tipo_funcao(10,numero_funcoes)
    funcoes_pertinencia = []
    for chave in funcoes.dominios.keys():
        funcoes_pertinencia.append(funcoes.dominios[chave])
        
    vetor_funcoes_z = [[random.uniform(-1, 1), random.uniform(-1, 1)] for _ in range(numero_funcoes)]
    valores_anteriores_z = copy.deepcopy(vetor_funcoes_z)

    erros = []
    menor_erro = math.inf

    geracao_atual = 0
    melhor_ger = geracao_atual

    z = calcular_z(x, funcoes_pertinencia, vetor_funcoes_z,tipo_funcao)
    menor_z = copy.deepcopy(z)
    calcular_erro(z, f_x, erros)
    resultado = check_erro(menor_erro, geracao_atual, erros, z)
    if resultado is not None:
        menor_z, menor_erro, melhor_ger = resultado

    ganho = 1
    multiplicador = 1

    while menor_erro > erro_minimo and ganho > 0.01*erro_minimo:
        for i in range(numero_funcoes):
            for j in range(2):
                geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger,tipo_funcao)

                while(erros[-2] > erros[-1]):
                    valores_anteriores_z = copy.deepcopy(vetor_funcoes_z)
                    geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger,tipo_funcao)

                multiplicador *= -1

                vetor_funcoes_z = copy.deepcopy(valores_anteriores_z)
                
                geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger,tipo_funcao)

                while(erros[-2] > erros[-1]):
                    valores_anteriores_z = copy.deepcopy(vetor_funcoes_z)
                    geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger,tipo_funcao)

                multiplicador *= -1

                vetor_funcoes_z = copy.deepcopy(valores_anteriores_z)
        ganho /= 2

    return menor_erro, erros, funcoes_pertinencia, vetor_funcoes_z

def plotar_graficos(x, f_x, zs, erros):

    # Plotar a função
    plt.figure(figsize=(10, 5))
    plt.plot(x, f_x, label=r'$f(x) = e^{-\frac{x}{5}} \sin(3x) + 0.5 \sin(x)$')
    i = 0
    for key in zs.keys():
        plt.plot(x, zs[key], label=key)
        i += 1
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Função f(x) e aproximações no intervalo [0, 10]")
    plt.legend()
    plt.grid(True)
    # plt.show()
    plt.show(block=False)

    # # Plotar o erro
    plt.figure(figsize=(10, 5))
    for key in erros.keys():
        plt.plot(np.linspace(0, len(erros[key]) - 1, len(erros[key])), erros[key], label=key)
    plt.xlabel("Geração")
    plt.ylabel("Erro")
    plt.title("Erro x Geração")
    plt.legend()
    plt.grid(True)
    plt.show()

erros = {}
erros_min = {}
pertinencias = {}
funcoes_z = {}
zs = {}

x = np.linspace(0, 10, 100)
f_x = np.exp(-x / 5) * np.sin(3 * x) + 0.5 * np.sin(x)

for funcao in [9]:
    for erro in [0.1]:
        print(f"{funcao} funções de pertinência e erro mínimo {erro}")
        erro_aux = []
        vet_erro_aux = []
        funcao_aux = []
        vetor_z_aux = []
        for i in range(10): # Número de testes
            print(f"Iteração {i}")
            menor_erro, vet_erros, funcoes_pertinencia, vetor_funcoes_z = aproximar(x,f_x,funcao, erro, fp.triangular)
            erro_aux.append(menor_erro)
            vet_erro_aux.append(vet_erros)
            funcao_aux.append(funcoes_pertinencia)
            vetor_z_aux.append(vetor_funcoes_z)
        media_erro_aux = np.mean(erro_aux)
        desvio_erro_aux = np.std(erro_aux)
        print(f'Média de erro_aux: {media_erro_aux:.4}')
        print(f'Desvio padrão de erro_aux: {desvio_erro_aux:.4}')
        tamanhos_vetores = [len(vetor) for vetor in vet_erro_aux]
        media_tamanhos = np.mean(tamanhos_vetores)
        desvio_tamanhos = np.std(tamanhos_vetores)
        print(f'Média dos tamanhos em vet_erro_aux: {media_tamanhos:.2f}')
        print(f'Desvio padrão dos tamanhos em vet_erro_aux: {desvio_tamanhos:.2f}')
        indice_menor_erro = erro_aux.index(min(erro_aux))
        print(f'{min(erro_aux):.4} & {media_erro_aux:.4} & {desvio_erro_aux:.4} & {media_tamanhos:.2f} & {desvio_tamanhos:.2f}')
        print(f"Menor erro encontrado {funcao} - {erro}: {min(erro_aux):.4}")
        erros[f"{funcao} funções de pertinência e erro mínimo {erro}"] = vet_erro_aux[indice_menor_erro]
        erros_min[f"{funcao} funções de pertinência e erro mínimo {erro}"] = erro_aux[indice_menor_erro]
        pertinencias[f"{funcao} funções de pertinência e erro mínimo {erro}"] = funcao_aux[indice_menor_erro]
        funcoes_z[f"{funcao} funções de pertinência e erro mínimo {erro}"] = vetor_z_aux[indice_menor_erro]
        zs[f"{funcao} funções de pertinência e erro mínimo {erro}"] = calcular_z(x,funcao_aux[indice_menor_erro],vetor_z_aux[indice_menor_erro],fp.triangular)

plotar_graficos(x, f_x, zs, erros)


