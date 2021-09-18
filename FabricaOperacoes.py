from Adicao import Adicao
from Subtracao import Subtracao
from Multiplicacao import Multiplicacao
from Divisao import Divisao

class FabricaOperacoes(object):
    
    def criar(self, operador):
        if (operador == 'soma'):
            return Adicao()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()
        elif (operador == 'divisao'):
            return Divisao()
        