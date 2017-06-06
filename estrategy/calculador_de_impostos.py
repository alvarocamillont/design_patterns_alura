from orcamento import Orcamento
from impostos import calcula_ISS, calcula_ICMS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, calcula_imposto):
        valor = calcula_imposto(orcamento)
        print(valor)


if __name__ == '__main__':
    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    # imprime 50
    calculador_de_impostos.realiza_calculo(orcamento, calcula_ICMS)
    # imprime 30
    calculador_de_impostos.realiza_calculo(orcamento, calcula_ISS)
