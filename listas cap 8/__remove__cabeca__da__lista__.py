
#A cabeca da lista e removida por referencia, sem ser necessario retornar

def removeCabeca(lista):
    del lista[0]

lista = [0,1,2,3,4,5,6,7,8,9]

removeCabeca(lista)
print(lista)

