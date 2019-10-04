
import math


def calculaArea(raio):
    area = math.pi * raio ** 2
    return area



raio = float(input('Digite o valor do raio do circulo: '))
print('A área do circulo com o raio {0} é: {1}'.format(str(raio),str(calculaArea(raio))))

