
def percorrendoString(palavra):
    index = 0
    while(index < len(palavra)):
        print(palavra[index])
        index = index + 1

palavra = input('Digite uma palavra: ')
percorrendoString(palavra)