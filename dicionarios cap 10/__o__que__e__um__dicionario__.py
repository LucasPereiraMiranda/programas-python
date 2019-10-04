
#Os tipos compostos que você aprendeu - strings, listas e tuplas - utilizam inteiros como indices.
#Os dicionarios possibilitam mapear um certo dado por qualquer outro tipo de dado, como indice


#dicionario vazio
dicionario = {}

dicionario['one'] = 'uno'
dicionario['two'] = 'dos'

print('Dicionario 1: ',dicionario)

#outra maneira de criar o dicionario é esta:
#a ordem no dicionario nao importa, ja qu os indices nao sao numericos

dicionario2 = {'one':'uno','two':'dos','three':'tres'}

print('Dicionario 2: ',dicionario2)

#buscando um elemento no dicionario:

print('Segundo elemento: ', dicionario2['two'])
