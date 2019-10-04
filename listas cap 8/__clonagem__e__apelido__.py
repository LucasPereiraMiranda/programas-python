

#quando programamos em python, pode existir a necessidade de obter uma copia de uma lista, perdendo a referência da mesmo.
# já que ao mudar a, b será mudado


#processo de apelido
a = [1,2,3]
b = a
b[0] = 5

#ao printar a, o valor da posicao 0 não será mais 1, mas sim 5
print('lista a com o processo de apelido: ',a)

#para fazer a clonagem e consequentemente perdermos a referencia entre a e b, devemos fazer o seguinte processo de clonagem
#usando fatiamento

a = [1,2,3]
b = a[:]
b[0] = 5

#ao printar a, veremos que ela não foi modificada, como no apelido do primeiro exemplo

print('lista a com o processo de clonagem: ',a)
