

def find(frase,padrao):
    index = 0
    while(index < len(frase)):
        if(padrao == frase[index]):
            return index
        index = index + 1
    return -1

frase = input('Digite uma frase: ')
padrao = input('Digite um caractere padrao a ser identificado: ')
print('Identificado em: {0}'.format(str(find(frase,padrao))))