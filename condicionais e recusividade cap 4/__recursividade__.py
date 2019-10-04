
def anoNovo(tempoRestante):
    if(tempoRestante == 0):
        print('Fogos de artificio!!! Tum Tum Pow Truwww')
        print('Feliz ano novo Lucas!!!')

    else:
        print(tempoRestante)
        anoNovo(tempoRestante - 1)

tempoRestante = int(input('Digite o tempo que falta para chegarmos ao ano novo:  '))

anoNovo(tempoRestante)

print('Fim do programa!')
