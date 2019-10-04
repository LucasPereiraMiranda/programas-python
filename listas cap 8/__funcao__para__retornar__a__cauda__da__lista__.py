
#o operador fatia gera uma nova lista, perdendo totalmente a referencia sobre a lista anterior

def obterCauda(lista):
    return lista[1:]

listaNumerica = [0,1,2,3,4,5,6,7,8,9]

print('a cauda da lista e: ',obterCauda(listaNumerica))