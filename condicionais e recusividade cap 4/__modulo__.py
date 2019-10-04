def calculaResto(numero1, numero2):
    return numero1 % numero2


numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero'))

print('O módulo de {0} por {1} é : {2}'.format(str(numero1), str(numero2), str(calculaResto(numero1, numero2))))

print('Fim do programa!')
