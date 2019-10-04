
def verificaPar(numero):
    if(numero % 2 == 0):
        return 'verdadeiro'
    else:
        return 'falso'

numero = int(input('Digite um numero:  '))
print(verificaPar(numero))

