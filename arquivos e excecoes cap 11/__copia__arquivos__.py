
def copiando():
    origem = open('origem.txt', 'r')
    destino = open('destino.txt', 'w')
    texto = origem.read()
    destino.write(texto)
    origem.close()
    destino.close()

print('     Seja bem-vindo(a) ao programa de copia de arquivos\n')
i = 0
origem = open('origem.txt','w')
destino = open('destino.txt','w')
while(1):
    linha = input('Digite o conteudo da linha {0}: '.format(str(i+1)))
    linha = linha +'\n'
    i=i+1
    origem.write(linha)
    escolha = int(input('deseja continuar escrevendo linhas no arquivo original? 0-não 1-sim: '))
    if(escolha == 1):
        continue
    else:
        break

origem.close()
destino.close()

copiando()
destino = open('destino.txt','r')
print('Contudo do arquivo destino:\n\n',destino.read())

destino.close()