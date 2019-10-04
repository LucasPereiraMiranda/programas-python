
from operator import itemgetter

#verifica o numero de ocorrencias de letras em uma string e salva em um dicionario


contadorLetras = {}

stringAnalisada = 'missisipi'

for letra  in stringAnalisada:
    contadorLetras[letra] = contadorLetras.get(letra,0) + 1

print(contadorLetras)

#Podemos ordenar o dicionario pelas letras, usando o sort()

copiaDicionario = contadorLetras.items()

print(sorted(copiaDicionario,key=itemgetter(0))) # 0 para ordenar segundo o indice
                                                 # 1 para ordenar segundo o valor
