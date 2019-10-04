
import math

def tabela(numero):
    x = 1.0
    while(x <= numero) :
        print(numero,'/t',math.log(numero))
        numero = numero - 1

numero = float(input('Digite um numero: '))
tabela(numero)
print('Fim do programa!')
