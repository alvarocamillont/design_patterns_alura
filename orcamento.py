class Orcamento(object):
    """
    Inicializado da classe
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
