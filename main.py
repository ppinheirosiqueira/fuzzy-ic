import fuzzyficador as fz

def __main__():
    dom_x = [0,100]
    funcoes = dominio_triangular(dom_x,4)
    print(funcoes)
    for chave in funcoes.keys():
        print(fz.func_triangular(1,funcoes[chave][0],funcoes[chave][1],funcoes[chave][2]))
    funcoes = dominio_triangular_complementares(dom_x,4)
    print(funcoes)
    for chave in funcoes.keys():
        print(fz.func_triangular(1,funcoes[chave][0],funcoes[chave][1],funcoes[chave][2]))
    funcoes = dominio_trapezoidal(dom_x,3)
    print(funcoes)
    for chave in funcoes.keys():
        print(fz.func_trapezoidal(1,funcoes[chave][0],funcoes[chave][1],funcoes[chave][2],funcoes[chave][3]))

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

if __name__ == "__main__":
    __main__()