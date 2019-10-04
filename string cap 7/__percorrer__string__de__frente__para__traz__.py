

def frenteParaTras(palavra):
    index = len(palavra)
    while(0 < index):
        print(palavra[index - 1])
        index = index - 1

palavra = input('Digite uma palavra: ')
frenteParaTras(palavra)