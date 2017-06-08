from abc import ABCMeta, abstractclassmethod


class Template_de_imposto_condicional(metaclass=ABCMeta):

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractclassmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractclassmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractclassmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS():
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS():
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICPP(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False


