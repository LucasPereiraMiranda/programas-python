

def criandoPalavras():
    prefixo = 'JKLMNOPQ'

    for letra in prefixo:
        if(letra == 'O' or letra == 'Q') :
            sulfixo = 'uack'
            print(letra + sulfixo)
        else:
            sulfixo = 'ack'
            print(letra + sulfixo)

criandoPalavras()