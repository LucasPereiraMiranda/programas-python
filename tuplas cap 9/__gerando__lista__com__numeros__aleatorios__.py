
import random

def listaAleatoria(tamanho):
    lista = [0] * tamanho
    for i in range(tamanho):
        lista[i] = random.random()
    return lista

def exibir(lista):
    print(lista)

def contandoNumerosIntervalo(lista,inferior,superior):
    contador = 0
    for valor in lista:
        if inferior < valor < superior:
            contador = contador + 1
        else :
            continue
    return contador

tamanho = int(input('Digite o tamanho da lista com numeros aleatorios a ser criada: '))
inferior = float(input('Digite o intervalo inferior: '))
superior = float(input('Digite o intervalo superior: '))

lista = listaAleatoria(tamanho)
exibir(lista)

print('O numero de valores dentro do intervalo é: ',contandoNumerosIntervalo(lista,inferior,superior))

