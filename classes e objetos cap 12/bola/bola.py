

__author__ = 'Lucas Pereira Miranda'

class Bola():

    def __init__(self,cor, circunferencia,material):
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material

    def mostraCor(self):
        return self._cor

    def trocaCor(self,cor):
        self._cor = cor



nike_model_one = Bola('Preta',0.50,'Sintético')

print('cor antiga: {0}'.format(str(nike_model_one.mostraCor())))

nova_cor = str(input('Digite a nova cor da bola:'))
nike_model_one.trocaCor(nova_cor)
print('nova cor: {0}'.format(str(nike_model_one.mostraCor())))
