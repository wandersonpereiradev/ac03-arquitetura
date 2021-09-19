import unittest
from Calculadora import Calculadora

class TestAdicao(unittest.TestCase):
    def teste_com_sucesso(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(8, 3, 'soma')
        self.assertEqual(resultado, 11)

    def teste_com_erro(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(5, 3, 'soma')
        self.assertEqual(resultado, 11)

    def teste_com_type_error(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(8, "3", 'soma')
        return self.assertEqual(resultado, 11)


if __name__ == '__main__':
    unittest.main()
