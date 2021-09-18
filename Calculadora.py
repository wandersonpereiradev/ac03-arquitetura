from FabricaOperacoes import *

class Calculadora(object):
    def calcular(self, valor1, valor2, operacao):
        fabrica = FabricaOperacoes()
        operacao = fabrica.criar(operacao)
        if (operacao == None):
            return 0
        else:
            resultado = operacao.executar_operacao(valor1, valor2)
            return resultado