# calculador_de_descontos.py
from descontos import Desconto_por_cinco_itens
from descontos import Desconto_por_mais_de_quinhentos_reais
""" Aplicação do Padrão Chain of Responsability """


class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens().calcular(orcamento)
        if(desconto == 0):
            desconto = Desconto_por_mais_de_quinhentos_reais().calcular(orcamento)

        # mais um if que testa se desconto é 0 e aplica aplica o desconto

        return desconto

        # outras possíveis regras aqui


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print(f'Desconto calculado :{desconto}')
