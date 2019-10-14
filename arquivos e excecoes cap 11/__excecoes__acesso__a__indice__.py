
__author__ = 'Lucas Pereira Miranda'
__date__ = '13/03/1998'

lista = ['lucas',[1,2,3],[4,5,6]]

#vamos obter um indice inexistente na lista, gerando uma excecao

print('excecao ao acessar indice inexistente: ')

try:
    print(lista[8])
except Exception as e:
    print(e)
