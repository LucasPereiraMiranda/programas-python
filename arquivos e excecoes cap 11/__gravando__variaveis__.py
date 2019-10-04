
arquivo = open('arquivo.txt','w')
variavel = input('Digite algo a ser escrito no arquivo: ')
arquivo.write(variavel)
arquivo.close()

arquivo = open('arquivo.txt','r')
texto = arquivo.read()
print("O texto contido no arquivo é:\n\n",texto)


