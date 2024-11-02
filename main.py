import fuzzyficador as fz

def print_list(valores:list):
    return [f"{valor:.2f}" for valor in valores]

def print_pertinencias(pertinencias:list):
    for valor in pertinencias:
        print(f"Para o valor {valor}: ")
        for funcao in pertinencias[valor]:
            print(f"Na função {funcao}: {print_list(pertinencias[valor][funcao])}")
        print("\n")

def __main__():
    fuzzyficador = fz.fuzzyficador(100,0,4)
    # pertinencias = fuzzyficador.get_pertinencia([28,76])
    # print_pertinencias(pertinencias)
    # fuzzyficador.plot_grafico("Gaussiana Dupla")
    # fuzzyficador.plot_graficos(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_complementos(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_grafico("Sino Generalizada")
    # fuzzyficador.plot_uniao("Sino Generalizada")
    # fuzzyficador.plot_unioes(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_intersecoes(fuzzyficador.funcoes.keys())
    #fuzzyficador.plot_grafico_t_normas("Exponencial", 5, 3458)
    fuzzyficador.plot_graficos_normas(fuzzyficador.funcoes.keys(), 5, 3458)

if __name__ == "__main__":
    __main__()