
#podemos criar as nossas excecoes
#o numero 6 nao e valido para esse programa, entao
#devemos bloquear a execucao deste numero, quando ele for utilizado

class ErroNumeroInvalido(Exception):
    pass

def entraNumero():
    numero = int(input('Digite um numero: '))
    if (numero==6):
        raise ErroNumeroInvalido('O numero ',numero,'nao pode ser usado nessa parte do programa')
    return numero

try:
    number = entraNumero()
    print('Deu tudo certo!!! O numero',number,'é valido para este programa!!! :)')
except ErroNumeroInvalido as detalhe:
    print(detalhe)