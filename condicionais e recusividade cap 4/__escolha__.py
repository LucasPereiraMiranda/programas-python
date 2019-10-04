
def escolha(palavra):
    if(palavra == 'funcao1'):
        funcao1()
    elif(palavra == 'funcao2'):
        funcao2()
    elif(palavra == 'funcao3'):
        funcao3()
    else:
        default()

def funcao1():
    print('voce escolheu a funcao 1')

def funcao2():
    print('voce escolheu a funcao2')

def funcao3():
    print('voce escolheu a funcao3')

def default():
    print('voce nao digitou uma string valida!')

print('digite funcao1 para entrar na opcao 1')
print('digite funcao2 para entrar na opcao 2')
print('digite funcao3 para entrar na opcao 3')
palavra = input('digite uma string: ')

escolha(palavra)

print('fim do programa!')