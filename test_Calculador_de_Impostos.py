import unittest

from calculador_de_impostos import CalculadorDeImpostos
from impostos import ICMS, ICPP, ISS, IKCV
from orcamento import Item, Orcamento


class CalculadorDeImpostosTestCase(unittest.TestCase):

    def setUp(self):
        self.orcamento = Orcamento()
        self.orcamento.adiciona_item(Item('Item A', 100.0))
        self.orcamento.adiciona_item(Item('Item B', 50.0))
        self.orcamento.adiciona_item(Item('Item C', 400.0))
        self.calculador_de_impostos = CalculadorDeImpostos()

    def test_realiza_calculo_ICMS(self):
        valor = self.calculador_de_impostos.realiza_calculo(self.orcamento, ICMS())
        self.assertEqual(valor, 33.0)

    def test_realiza_calculo_ISS(self):
        valor = self.calculador_de_impostos.realiza_calculo(self.orcamento, ISS())
        self.assertEqual(valor, 55.0)

    def test_realiza_calculo_ICPP(self):
        valor = self.calculador_de_impostos.realiza_calculo(self.orcamento, ICPP())
        self.assertEqual(valor, 38.5)

    def test_realiza_calculo_IKCV(self):
        valor = self.calculador_de_impostos.realiza_calculo(self.orcamento, IKCV())
        self.assertEqual(valor, 55)


if __name__ == '__main__':
    unittest.main()
