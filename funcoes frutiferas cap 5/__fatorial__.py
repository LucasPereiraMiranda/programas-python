

def fatorial(numero):
    if(numero == 0):
        return 1
    else:
        return numero * fatorial(numero - 1)


numero = int(input('Digite um numero: '))
print('o fatorial do numero {0} é: {1}'.format(str(numero),str(fatorial(numero))))
