
#Imprimindo os numeros pares contidos na lista gerada de 0 a numero -1

def funcao(numero):
    for num in range(numero):
        if num % 2 == 0:
            print(num)

numero = int(input('Digite um numero: '))
funcao(numero)
print('Fim do programa!')

