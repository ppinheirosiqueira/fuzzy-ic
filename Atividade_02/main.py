import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import math

def pertinencia_tri(x,a,b,c):
    if x <= a or x >= c:
        return 0.0

    if x <= b:
        return (x - a) / (b - a)
    
    return (c - x) / (c - b)

def pertinencia_gau(x, c, sigma):
    return math.e**((-(x-c)**2)/(2*sigma**2))

def criar_funcoes_pertinencia(diferenca, numero_de_funcoes):

    funcoes = []
    numero_de_divisoes = numero_de_funcoes - 1

    intervalo = diferenca/numero_de_divisoes

    sigma = intervalo/(2*math.sqrt(2*math.log(2,math.e)))

    for i in range(numero_de_funcoes):
        # funcoes.append([intervalo*(i-1), intervalo*(i), intervalo*(i+1)])
        funcoes.append([intervalo*i, sigma])

    return funcoes

def calcular_z(x,funcoes_pertinencia,vetor_funcoes_z):
    z = []
    for ponto in x:
        somatorio_cima = 0
        somatorio_baixo = 0
        for i in range(len(funcoes_pertinencia)):
            # pertinencia_ponto = pertinencia_tri(ponto,*funcoes_pertinencia[i])
            pertinencia_ponto = pertinencia_gau(ponto,*funcoes_pertinencia[i])
            somatorio_baixo += pertinencia_ponto
            somatorio_cima += pertinencia_ponto*vetor_funcoes_z[i][0] + vetor_funcoes_z[i][1]
        z.append(somatorio_cima/somatorio_baixo if somatorio_baixo != 0 else 1)
    return z

def calcular_erro(z, f_x, erros):
    erro = 0
    for i in range(len(f_x)):
        erro += (f_x[i] - z[i])**2

    erro = erro/len(f_x)
    erro = erro**(1/2)
    erros.append(erro)

def att_funcoes(funcoes_pertinencia, vetor_funcoes_z, i, j, multiplicador, ganho, geracao_atual):
    if j > 1: 
        vetor_funcoes_z[i][j - 2] += multiplicador*ganho
    else:
        funcoes_pertinencia[i][j] += multiplicador*ganho
        if j == 1:
            if funcoes_pertinencia[i][1] <= 0:
                funcoes_pertinencia[i][1] = 0.01
    return geracao_atual + 1

def check_erro(menor_erro, geracao_atual, erros, z):
    if erros[-1] < menor_erro:
        menor_z = copy.deepcopy(z)
        menor_erro = erros[-1]
        melhor_ger = geracao_atual
        return menor_z, menor_erro, melhor_ger
    
def att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger):
    geracao_atual = att_funcoes(funcoes_pertinencia, vetor_funcoes_z, i, j, multiplicador, ganho, geracao_atual)
    z = calcular_z(x, funcoes_pertinencia, vetor_funcoes_z)
    calcular_erro(z, f_x, erros)
    resultado = check_erro(menor_erro, geracao_atual, erros, z)
    if resultado is not None:
        menor_z, menor_erro, melhor_ger = resultado
    return geracao_atual, menor_z, menor_erro, melhor_ger

def aproximar(numero_funcoes, erro_minimo):
    # Definir o intervalo de x de 0 a 10 com um número suficiente de pontos
    x = np.linspace(0, 10, 100)

    # Definir a função f(x) = e^(-x/5) * sin(3x) + 0.5 * sin(x)
    f_x = np.exp(-x / 5) * np.sin(3 * x) + 0.5 * np.sin(x)

    funcoes_pertinencia = criar_funcoes_pertinencia(10, numero_funcoes)
    vetor_funcoes_z = [[random.uniform(-1, 1), random.uniform(-1, 1)] for _ in range(numero_funcoes)]

    valores_anteriores_funcoes = copy.deepcopy(funcoes_pertinencia)
    valores_anteriores_z = copy.deepcopy(vetor_funcoes_z)

    erros = []
    menor_erro = math.inf

    geracao_atual = 0
    melhor_ger = geracao_atual
    numero_teste_geracoes = numero_funcoes * (2 + len(funcoes_pertinencia[0]))
    maximo_geracoes = 100*numero_teste_geracoes

    z = calcular_z(x, funcoes_pertinencia, vetor_funcoes_z)
    menor_z = copy.deepcopy(z)
    calcular_erro(z, f_x, erros)
    resultado = check_erro(menor_erro, geracao_atual, erros, z)
    if resultado is not None:
        menor_z, menor_erro, melhor_ger = resultado

    ganho = 1
    multiplicador = 10

    while menor_erro > erro_minimo and geracao_atual - melhor_ger < maximo_geracoes:
        i = random.randint(0,numero_funcoes - 1)
        j = random.randint(0, 1 + len(funcoes_pertinencia[0]))

        geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger)

        while ((erros[-2] - erros[-1])/erros[-2] > 0.05*ganho):
            valores_anteriores_funcoes = copy.deepcopy(funcoes_pertinencia)
            valores_anteriores_z = copy.deepcopy(vetor_funcoes_z)
            geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger)

        multiplicador *= -1

        funcoes_pertinencia = copy.deepcopy(valores_anteriores_funcoes)
        vetor_funcoes_z = copy.deepcopy(valores_anteriores_z)
        
        geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger)

        while ((erros[-2] - erros[-1])/erros[-2] > 0.05*ganho):
            valores_anteriores_funcoes = copy.deepcopy(funcoes_pertinencia)
            valores_anteriores_z = copy.deepcopy(vetor_funcoes_z)
            geracao_atual, menor_z, menor_erro, melhor_ger = att_z_e_erro(i, j, x, funcoes_pertinencia, vetor_funcoes_z, f_x, erros, menor_erro, geracao_atual, multiplicador, ganho, menor_z, melhor_ger)

        multiplicador *= -1

        funcoes_pertinencia = copy.deepcopy(valores_anteriores_funcoes)
        vetor_funcoes_z = copy.deepcopy(valores_anteriores_z)

        if geracao_atual - melhor_ger > numero_teste_geracoes and ganho > 0.05*erro_minimo:
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

for funcao in [10]:
    for erro in [0.05, 0.01]:
        print(f"{funcao} funções de pertinência e erro mínimo {erro}")
        erro_aux = []
        vet_erro_aux = []
        funcao_aux = []
        vetor_z_aux = []
        for i in range(1): # Número de testes
            print(f"Iteração {i}")
            menor_erro, vet_erros, funcoes_pertinencia, vetor_funcoes_z = aproximar(funcao, erro)
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
        print(f'Média dos tamanhos em vet_erro_aux: {media_tamanhos:.4}')
        print(f'Desvio padrão dos tamanhos em vet_erro_aux: {desvio_tamanhos:.4}')
        indice_menor_erro = erro_aux.index(min(erro_aux))
        print(f'{media_erro_aux:.4} & {desvio_erro_aux:.4} & {media_tamanhos:6.4} & {desvio_tamanhos:6.4}')
        print(f"Menor erro encontrado {funcao} - {erro}: {min(erro_aux):.4}")
        erros[f"{funcao} funções de pertinência e erro mínimo {erro}"] = vet_erro_aux[indice_menor_erro]
        erros_min[f"{funcao} funções de pertinência e erro mínimo {erro}"] = erro_aux[indice_menor_erro]
        pertinencias[f"{funcao} funções de pertinência e erro mínimo {erro}"] = funcao_aux[indice_menor_erro]
        funcoes_z[f"{funcao} funções de pertinência e erro mínimo {erro}"] = vetor_z_aux[indice_menor_erro]
        zs[f"{funcao} funções de pertinência e erro mínimo {erro}"] = calcular_z(x,funcao_aux[indice_menor_erro],vetor_z_aux[indice_menor_erro])

plotar_graficos(x, f_x, zs, erros)


