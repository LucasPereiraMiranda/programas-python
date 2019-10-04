
#o seguinte dicionario contém o nome da fruta como indice e o numero de unidades como conteudo


inventario = {'abacaxi':430,'bananas':312,'laranjas':525,'peras':217}

print('antes de remover as peras: ',inventario)

#caso alguem compre todas as peras, podemos apaga-las do inventario:

del inventario['peras']

print('apos remover as peras: ',inventario)

#podemos tambem atualizar o valor das peras:

inventario['peras'] = 0

print('apos atualizar o valor da quantidade das peras: ',inventario)

#a funcao len funciona retornando o numero de pares-chaves contidos no dicionario

print('quantidade de pares chaves contidos no dicionario (inventario): ',len(inventario))
