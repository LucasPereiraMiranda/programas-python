
def verificacao(numero1,numero2):
    if(numero1 > numero2):
        print('O numero {0} é maior que o numero {1}'.format(str(numero1),str(numero2)))
    elif(numero1 < numero2 ):
        print('O numero {0} é menor que o numero {1}'.format(str(numero1), str(numero2)))
    else:
        print('O numero {0} é igual ao numero {1}'.format(str(numero1), str(numero2)))


numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero:  '))

verificacao(numero1,numero2)
print('Fim do programa!')
