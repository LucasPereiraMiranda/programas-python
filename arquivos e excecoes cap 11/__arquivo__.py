

primeiroArquivo = open('primeiro_arquivo.txt','w')
primeiroArquivo.write('Agora é a hora\n')
primeiroArquivo.write('De fechar o arquivo')
primeiroArquivo.close()

primeiroArquivo = open('primeiro_arquivo.txt','r')

texto = primeiroArquivo.read()

print(texto)

#read pode receber como parametro o numero de caracteres que ele pode ler read(9)

