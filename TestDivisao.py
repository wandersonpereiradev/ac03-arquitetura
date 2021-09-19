import unittest
from Calculadora import Calculadora

class TestDivisao(unittest.TestCase):
    def teste_com_sucesso(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(15, 5, 'divisao')
        self.assertEqual(resultado, 3)

    def teste_com_erro(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(15, 5, 'divisao')
        self.assertEqual(resultado, 11)

    def teste_com_type_error(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(15, "3", 'divisao')
        return self.assertEqual(resultado, 11)


if __name__ == '__main__':
    unittest.main()
