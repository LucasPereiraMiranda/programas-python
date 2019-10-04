
dicionario = {'bananas':1500}

while(1) :
    fruta = input('Digite a fruta a ser inserida no dicionario: ')
    quantidade = int(input('Digite a quantidade atual da fruta: '))
    dicionario[fruta] = quantidade
    validacaoDoWhile = int(input('deseja inserir mais elementos? 1 para sim, 0 para nao: '))
    if(validacaoDoWhile == 1):
        continue
    elif(validacaoDoWhile == 0):
        break
    else:
        validacaoDoWhile = int(input('Digite um valor valido: '))
        continue

print('O conteudo do dicionario é: ',dicionario)

#o metodo keys retorna o indice, ou seja, vai mostrar apenas indice de cada valor contido no dicionario
print(dicionario.keys())

#o metodo values vai retornar o conteudo de cada indice do dicionario
print(dicionario.values())

#o metodo items retorna os dois, na forma de uma lista de tuplas
print(dicionario.items())

#o metodo get retorna o elemento do indice solicitado pelo parametro do metodo
print('Vai exibir a quantidade de bananas: ',dicionario.get('bananas'))

#o operador in retorna um boolean informando se esta contido ou nao um valor no dicionario

print('Dicionario in : ','bananas' in dicionario)