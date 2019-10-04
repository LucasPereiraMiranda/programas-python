

tupla = (1,2,3,4,5,6,7,8,9,10)


#ao executarmos esse programa, obteremos uma mensagem de error
#tupla[0] = 0


#porem podemos substituir esta mesma tupla, por outra diferente

tupla2 = (0,) + tupla[:]

print(tupla2)