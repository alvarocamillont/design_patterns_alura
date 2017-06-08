from impostos import ICMS, ISS, IKCV, ICPP
from orcamento import Orcamento, Item
""" Aplicação do Padrão Strategy """


class CalculadorDeImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = round(imposto.calcula(orcamento), 2)
        return valor


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))
    calculador_de_impostos = CalculadorDeImpostos()

    print('ICMS e ISS')
    print(calculador_de_impostos.realiza_calculo(orcamento, ICMS()))
    print(calculador_de_impostos.realiza_calculo(orcamento, ISS()))

    print('ICPP, IKCV')
    print(calculador_de_impostos.realiza_calculo(orcamento, ICPP()))
    print(calculador_de_impostos.realiza_calculo(orcamento, IKCV(ICMS())))
