__author__ = 'Lucas Pereira Miranda'
__date__ = '14/10/2019'


class Bola:

    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor


nike_model_one = Bola('Preta', 0.50, 'Sintético')
print('cor antiga: {0}'.format(str(nike_model_one.cor)))
nike_model_one.cor = str(input('Digite a nova cor da bola:'))
print('nova cor: {0}'.format(str(nike_model_one.cor)))
