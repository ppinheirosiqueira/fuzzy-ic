import fuzzyficador as fz
import relacao
import composicao

def print_list(valores:list):
    return [f"{valor:.2f}" for valor in valores]

def print_pertinencias(pertinencias:list):
    for valor in pertinencias:
        print(f"Para o valor {valor}: ")
        for funcao in pertinencias[valor]:
            print(f"Na função {funcao}: {print_list(pertinencias[valor][funcao])}")
        print("\n")

def __main__():
    fuzzyficador = fz.fuzzyficador(0,100,5)
    # pertinencias = fuzzyficador.get_pertinencia([28,76])
    # print_pertinencias(pertinencias)
    # fuzzyficador.plot_grafico("Gaussiana Dupla")
    # fuzzyficador.plot_graficos(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_complementos(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_grafico("Sino Generalizada")
    # fuzzyficador.plot_uniao("Sino Generalizada")
    # fuzzyficador.plot_unioes(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_intersecoes(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_grafico_t_normas("Exponencial", 5, 3458)
    # fuzzyficador.plot_graficos_normas(fuzzyficador.funcoes.keys(), 5, 3458)
    fuzzyficador_2 = fz.fuzzyficador(0,40,4)
    #relacao.plot_relacoes(fuzzyficador,fuzzyficador_2,"Gaussiana",2,"Trapezoidal",3,["Norma T - Lukasiewicz","Norma S - Lukasiewicz","Mínimo de Zadeh", "Máximo de Zadeh"], 5, 3458)
    fuzzyficador_3 = fz.fuzzyficador(0,80,4)
    matriz_1 = relacao.get_valor_relacao(fuzzyficador, fuzzyficador_2, "Exponencial",2,"Gaussiana",3,"Norma S - Lukasiewicz", 5, 3458)
    matriz_2 = relacao.get_valor_relacao(fuzzyficador_2,fuzzyficador_3,"Gaussiana",2,"Sigmoidal",3,"Soma Probabilistica")
    composicao.plotar_composicoes(matriz_1,matriz_2)

if __name__ == "__main__":
    __main__()