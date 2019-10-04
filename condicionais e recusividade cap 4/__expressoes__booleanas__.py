

def comparacao(numero1,numero2):
    return numero2 == numero1


numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero:  '))

print('O numero {0} é igual ao numero {1}? -> {2}'.format(str(numero1),str(numero2),str(comparacao(numero1,numero2))))

print('Fim do programa!')
