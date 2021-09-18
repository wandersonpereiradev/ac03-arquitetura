import abc


class Operacao(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def operacao(self, valor1, valor2):
        pass