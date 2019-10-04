
import math

class __Ponto__:
    pass

def printFormatoPadrao(pontoInicial,pontoFinal):
    print('Ponto Inicial: ({0},{1})\nPonto Final: ({2},{3})'.format(str(pontoInicial.x),
                                str(pontoInicial.y),str(pontoFinal.x),str(pontoFinal.y)))

def calculaDistanciaEuclidiana(pontoInicial,pontoFinal):
    dx = pontoFinal.x - pontoInicial.x
    dy = pontoFinal.y - pontoInicial.y
    dQuadrado = dx**2 + dy**2
    resultado = math.sqrt(dQuadrado)
    return resultado

def verificaPontosIguais(pontoInicial,pontoFinal):
    return (pontoInicial.x == pontoFinal.x) and (pontoInicial.y == pontoFinal.y)

pontoInicial = __Ponto__()
pontoFinal = __Ponto__()

pontoInicial.x = float(input('Digite o valor de x no ponto inicial: '))
pontoInicial.y = float(input('Digite o valor de y no ponto inicial: '))

pontoFinal.x = float(input('Digite o valor de x no ponto final: '))
pontoFinal.y = float(input('Digite o valor de y no ponto final: '))

printFormatoPadrao(pontoInicial,pontoFinal)
print('A distancia entre os dois pontos é: ',calculaDistanciaEuclidiana(pontoInicial,pontoFinal))
print('Os pontos analisados são iguais? ',verificaPontosIguais(pontoInicial,pontoFinal))
