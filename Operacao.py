import abc


class Operacao(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def executar_operacao(self, valor1, valor2):
        pass