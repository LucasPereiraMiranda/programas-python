# Alisasing: sempre que duas variaveis referenciarem a um mesmo objeto, quando uma e alterada, afeta a outra

dicionario = {'Incrivel' : 'Lucas', 'Legal' : 'Ellen', 'Abencoada' : 'Erica'}

#Ao simplismente copiarmos, mantemos a referencia ao dicionario em ambas as variaveis (modificando em uma, modifica na outra)

mantendoReferencia = dicionario

print('Antes de remover: ',dicionario)

del mantendoReferencia['Legal']

print('printando o original, sem perder a referencia: ',dicionario)

#Devemos utilizar o metodo copy, para perdermos a referencia ao endereco da variavel original

dicionario2 = {'Incrivel' : 'Lucas', 'Legal' : 'Ellen', 'Abencoada' : 'Erica'}

perdendoReferencia = dicionario2.copy()

print()
print('perdendoReferencia: ',perdendoReferencia)

del perdendoReferencia['Legal']

print('printando o original, perdendo a referencia: ',dicionario2)

