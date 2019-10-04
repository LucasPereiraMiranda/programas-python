
#Quando salvamos estruturas de dados em arquivos, podemos ter dificuldades em
#carregá-los novamente para a execução de um programa. Já que convertemos tudo
#para str
#Para auxiliar em trazer novamente estas estruturas, devemos utilizar o pickle

import pickle

f = open("test.pck", "w")

#Para armazenar uma estrutura de dados, use o método dump e então feche o arquivo do modo usual

pickle.dump('12.3', f)
pickle.dump('[1,2,3]', f)
f.close()

#Então, podemos abrir o arquivo para leitura e carregar as estruturas de dados que foram descarregadas (dumped):

f = open("test.pck", "r")
x = pickle.load(f)
print(x)