# coding:utf-8

import math

__author__ = "Lucas Pereira Miranda"


class Quadrado():

    def __init__(self, lado):
        self._lado = lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, lado):
        self._lado = lado

    def obter_area_quadrado(self):
        return math.pow(self._lado, 2)


quad = Quadrado(150)
print('O lado do quadrado vale: {0}'.format(str(quad.lado)))
print('A área do quadrado vale: {0}'.format(str(quad.obter_area_quadrado())))
quad.lado = float(input('Digite o novo lado do quandrado:'))
print('O lado do quadrado vale: {0}'.format(str(quad.lado)))
print('A área do quadrado vale: {0}'.format(str(quad.obter_area_quadrado())))
