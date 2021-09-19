import unittest
from Calculadora import Calculadora

class TestMultiplicacao(unittest.TestCase):
    def teste_com_sucesso(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(7, 3, 'multiplicacao')
        self.assertEqual(resultado, 21)

    def teste_com_erro(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(5, 3, 'multiplicacao')
        self.assertEqual(resultado, 11)

    def teste_com_type_error(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(8, "3", 'multiplicacao')
        return self.assertEqual(resultado, 11)


if __name__ == '__main__':
    unittest.main()
