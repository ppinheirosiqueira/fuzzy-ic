import fuzzyficador as fz
import dominio as dom

funcoes_de_pertinencia = {
    "Triangular não complementar": fz.func_pert_triangular,
    "Triangular complementar": fz.func_pert_triangular,
    "Trapezoidal": fz.func_pert_trapezoidal,
    "Gaussiana": fz.func_pert_gaussiana,
    "Sigmoidal": fz.func_pert_sigmoidal,
    "Sino Generalizada": fz.func_pert_sino_generalizada,
    "Z Shaped": fz.func_pert_z_shaped,
    "S Shaped": fz.func_pert_s_shaped,
}

def __main__():
    dom_x = [0,100]
    dominios = {
        "Triangular não complementar": dom.dominio_triangular(dom_x,4),
        "Triangular complementar": dom.dominio_triangular_complementares(dom_x,4),
        "Trapezoidal": dom.dominio_trapezoidal(dom_x,4),
        "Gaussiana": dom.dominio_gaussiana(dom_x,4),
        "Sigmoidal": dom.dominio_sigmoidal(dom_x,4),
        "Sino Generalizada": dom.dominio_sino_generalizada(dom_x,4),
        "Z Shaped": dom.dom_shapeds(dom_x,4),
        "S Shaped": dom.dom_shapeds(dom_x,4),
    }

    valor_testado = 25

    for chave in dominios.keys():
        print(f"Os dominios da {chave} foram determinados: {dominios[chave]}")
        for funcao in dominios[chave].keys():
            print(f"O valor {valor_testado} tem pertinência {funcoes_de_pertinencia[chave](valor_testado,*dominios[chave][funcao])} no dominio {dominios[chave][funcao]}")
        print('\n')

if __name__ == "__main__":
    __main__()