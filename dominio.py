import math

def dominio_triangular(limites:list[float],numero_de_funcoes:int) -> dict:
    if limites[0] > limites[1]:
        raise ValueError("Erro: Não é possível ter um limite inferior maior que o superior")
    
    numero_de_divisoes = numero_de_funcoes + 1

    intervalo = (limites[1] - limites[0])/numero_de_divisoes

    dominios = {}

    for i in range(numero_de_funcoes):
        dominios[i] = [intervalo*i, intervalo*(i+1), intervalo*(i+2)]

    return dominios

def dominio_triangular_complementares(limites:list[float],numero_de_funcoes:int) -> dict:
    if limites[0] > limites[1]:
        raise ValueError("Erro: Não é possível ter um limite inferior maior que o superior")
    
    numero_de_divisoes = numero_de_funcoes - 1

    intervalo = (limites[1] - limites[0])/numero_de_divisoes

    dominios = {}

    for i in range(numero_de_funcoes):
        if i == 0:
            dominios[i] = [limites[0], limites[0], intervalo]
        elif i == numero_de_funcoes - 1:
            dominios[i] = [limites[1] - intervalo, limites[1], limites[1]]
        else:
            dominios[i] = [intervalo*(i-1), intervalo*(i), intervalo*(i+1)]

    return dominios

def dominio_trapezoidal(limites:list[float],numero_de_funcoes:int) -> dict:
    if limites[0] > limites[1]:
        raise ValueError("Erro: Não é possível ter um limite inferior maior que o superior")

    numero_de_divisoes = 2*numero_de_funcoes - 1

    intervalo = (limites[1] - limites[0])/numero_de_divisoes

    dominios = {}

    for i in range(numero_de_funcoes):
        if i == 0:
            dominios[i] = [limites[0], limites[0], intervalo, intervalo*2]
        elif i == numero_de_funcoes - 1:
            dominios[i] = [limites[1] - intervalo*2, limites[1] - intervalo, limites[1], limites[1]]
        else:
            dominios[i] = [intervalo*i, intervalo*(i + 1), intervalo*(i+2), intervalo*(i+3)]

    return dominios

def dominio_gaussiana(limites:list[float],numero_de_funcoes:int) -> dict:
    if limites[0] > limites[1]:
        raise ValueError("Erro: Não é possível ter um limite inferior maior que o superior")
    
    numero_de_divisoes = numero_de_funcoes - 1

    intervalo = (limites[1] - limites[0])/numero_de_divisoes

    dominios = {}

    # O desvio padrão será uma loucura de calcular
    # Imaginando que os intervalos são de tamanho X
    # Quero que em X/2, ou seja, bem no meio das duas primeiras curvas, a soma das pertinências seja próxima de 1
    # Pela fórmula da gaussiana isso da que o desvio padrão é igual a
    # σ= x / 2sqr(2ln(2))

    sigma = intervalo/(2*math.sqrt(2*math.log(2,math.e)))

    for i in range(numero_de_funcoes):
        dominios[i] = [intervalo*i, sigma]

    return dominios

def dominio_sigmoidal(limites:list[float],numero_de_funcoes:int) -> dict:
    if limites[0] > limites[1]:
        raise ValueError("Erro: Não é possível ter um limite inferior maior que o superior")
    
    numero_de_divisoes = numero_de_funcoes - 1

    intervalo = (limites[1] - limites[0])/numero_de_divisoes

    dominios = {}

    # A inclinação é difícil mensurar
    # Dado que ao contrário da Gaussiana, esta ao subir ficará em 1 para sempre
    # Ou seja, todos os valores altos numa sigmoidal acabam em 1 de pertinência
    # De qualquer forma, vou colocar como atingindo o máximo em meio intervalo
    # Ou seja, é uma inclinação que começa em 0 e vai até 1 em intervalo/2

    inclinacao = 2/intervalo

    for i in range(numero_de_funcoes):
        dominios[i] = [intervalo*i, inclinacao]

    return dominios

def dominio_sino_generalizada(limites:list[float],numero_de_funcoes:int) -> dict:
    if limites[0] > limites[1]:
        raise ValueError("Erro: Não é possível ter um limite inferior maior que o superior")

    numero_de_divisoes = numero_de_funcoes - 1

    intervalo = (limites[1] - limites[0])/numero_de_divisoes

    dominios = {}

    # Como é arbitrário o valor da largura e da suavidade
    # Largura vou colocar como 1/4 do intervalo
    # Suavidade vou colocar como 1/2 do intervalo

    met_int = 0.5*intervalo
    um_quarto_int = 0.25*intervalo

    for i in range(numero_de_funcoes):
        dominios[i] = [um_quarto_int,met_int,intervalo*i]

    return dominios

def dom_shapeds(limites:list[float],numero_de_funcoes:int) -> dict:
    if limites[0] > limites[1]:
        raise ValueError("Erro: Não é possível ter um limite inferior maior que o superior")
    
    numero_de_divisoes = numero_de_funcoes + 1

    intervalo = (limites[1] - limites[0])/numero_de_divisoes

    dominios = {}

    for i in range(numero_de_funcoes):
        dominios[i] = [intervalo*(i+1),intervalo*(i+2)]

    return dominios