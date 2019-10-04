

def fibonacci(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)


numero = int(input('Digite um numero: '))
print('o numero referente a sequencia de fibonacci de {0} é {1}'.format(str(numero),str(fibonacci(numero))))