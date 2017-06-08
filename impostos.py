class ISS():
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS():
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICPP(object):
    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return orcamento.valor * 0.05


class IKCV(object):
    def calcula(self, orcamento):
        if orcamento.valor > 500 and self.__tem_item_maior_que_100(orcamento):
            return orcamento.valor * 0.1
        else:
            return orcamento.valor * 0.06

    def __tem_item_maior_que_100(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False


