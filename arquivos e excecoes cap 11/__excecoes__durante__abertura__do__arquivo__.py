

#para tratar uma excecao, usamos a clausula try e except

nomeArquivo = input('digite o nome do arquivo: ')

try:
    arquivo = open(nomeArquivo,'r')
except:
    print('nao existe arquivo chamado {0}'.format(str(nomeArquivo)))

