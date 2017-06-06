from impostos import calcula_ISS, calcula_ICMS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        if 'ICMS' == imposto:
            icms_calculado = calcula_ICMS(orcamento)
            print(icms_calculado)
        elif 'ISS' == imposto:
            iss_calculado = calcula_ISS(orcamento)
            print(iss_calculado)


if __name__ == '__main__':

    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, 'ICMS')  # imprimie 50.0
    calculador_de_impostos.realiza_calculo(orcamento, 'ISS')  # imprime 30.0
