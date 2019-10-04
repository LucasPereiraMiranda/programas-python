
def validacao(dia,mes,ano):

    if((1 <= dia <= 31) and (1 <= mes <= 12)):
        print('A data {0}/{1}/{2} está validada'.format(str(dia),str(mes),str(ano)))
    else:
        print('A data {0}/{1}/{2} não está validada'.format(str(dia),str(mes),str(ano)))

verificacao = 1
while(verificacao == 1):
    try:
        dia = int(input('dia: '))
        mes = int(input('mes: '))
        ano = int(input('ano: '))
        verificacao = 0
    except:
        print('Digite numeros, e nao strings')
        continue

validacao(dia,mes,ano)
print('Fim do programa!')
