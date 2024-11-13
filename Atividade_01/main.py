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
    fuzzyficador = fz.fuzzyficador(0,100,4)
    # pertinencias = fuzzyficador.get_pertinencia([28,76])
    # print_pertinencias(pertinencias)
    # fuzzyficador.plot_grafico("Trapezoidal")
    # fuzzyficador.plot_graficos(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_complemento("Pi Shaped")
    # fuzzyficador.plot_complementos(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_grafico("Sino Generalizada")
    # fuzzyficador.plot_uniao("Pi Shaped")
    # fuzzyficador.plot_unioes(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_intersecoes(fuzzyficador.funcoes.keys())
    # fuzzyficador.plot_grafico_t_normas("Exponencial", 5, 3458)
    # fuzzyficador.plot_graficos_normas(fuzzyficador.funcoes.keys(), 5, 3458)
    fuzzyficador_2 = fz.fuzzyficador(0,40,4)
    # relacao.plot_relacoes(fuzzyficador,fuzzyficador_2,"Gaussiana",2,"Trapezoidal",3,["Norma T - Lukasiewicz","Norma S - Lukasiewicz","Mínimo de Zadeh", "Máximo de Zadeh"], 5, 3458)
    fuzzyficador_3 = fz.fuzzyficador(0,80,4)
    matriz_1 = relacao.get_valor_relacao(fuzzyficador, fuzzyficador_2, "Gaussiana",2,"Trapezoidal",3,"Norma S - Lukasiewicz", 5, 3458)
    matriz_2 = relacao.get_valor_relacao(fuzzyficador_2,fuzzyficador_3,"Trapezoidal",2,"Sigmoidal",3,"Mínimo de Zadeh")
    composicao.plotar_composicoes(matriz_1,matriz_2,"1º Domínio - Guassiana-2 com o 2º Domínio - Trapezoidal-3, com Norma S - Lukasiewicz","2º Domínio - Trapezoidal-3 com o 3º Domínio - Sigmoidal-3, com Mínimo de Zadeh")

if __name__ == "__main__":
    __main__()