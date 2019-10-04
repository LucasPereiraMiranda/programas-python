

#passar uma lista como parametro, passa-se uma referencia da lista, e nao uma copia


def cabeca(lista):
    return lista[0]


lista = ['primeiro','segundo','terceiro','quarto','quinto']

print('dados contidos na lista: ',lista)
print('cabeca da lista: ',cabeca(lista))



