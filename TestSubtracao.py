import unittest
from Calculadora import Calculadora

class TestSubtracao(unittest.TestCase):
    def teste_com_sucesso(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(8, 3, 'subtracao')
        self.assertEqual(resultado, 5)

    def teste_com_erro(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(5, 3, 'subtracao')
        self.assertEqual(resultado, 11)

    def teste_com_type_error(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(8, "3", 'subtracao')
        return self.assertEqual(resultado, 5)


if __name__ == '__main__':
    unittest.main()
