
def contador(frase,caractere):
    count = 0
    for letra in frase:
        if(letra == caractere):
            count = count +1
        else:
            continue
    return count



frase = input('Digite uma frase: ')
caractere = input('Digite o caractere a ser verificado: ')
print('O numero de vezes que o caractere {0} apareceu em {1} é: {2}'.format(str(caractere),str(frase),str(contador(frase,caractere))))

