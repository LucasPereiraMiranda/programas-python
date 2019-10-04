
def obterTamanho(variavelStr):
    return len(variavelStr)


variavelStr = input('Digite uma palavra: ')
print('O tamanho da String {0} é: {1} caracteres'.format(str(variavelStr),obterTamanho(variavelStr)))