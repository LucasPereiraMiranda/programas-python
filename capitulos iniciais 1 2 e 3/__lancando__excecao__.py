

class InvalidacaoTexto(Exception):
    pass

def eMinusculo(string):
    if(not str.islower(string)):
        raise InvalidacaoTexto('O texto possui caracteres/digitos que sao maiusculos!')
    else:
        print('O texto é 100% minusculo')


try:
    string = input('Digite um texto: ')
    str.islower(string)
    eMinusculo(string)

except InvalidacaoTexto as message:
    print(message)



