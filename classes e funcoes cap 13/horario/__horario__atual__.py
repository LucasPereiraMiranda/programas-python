
class Horario:
    pass

class ExcecaoTempo(Exception):
    pass


def validacaoHorario(horarioAtual,horarioDoPao):
    if(horarioAtual.segundos >= 60 or horarioAtual.segundos <= 0
        or horarioAtual.minutos >=60 or horarioAtual.minutos <= 0
            or horarioAtual.horas >= 24 or horarioAtual.horas <= 0):
        raise(ExcecaoTempo('Você digitou o horario atual inválido: {0}:{1}:{2}'.format(str(horarioAtual.segundos)
                                                                                       ,str(horarioAtual.minutos)
                                                                                       ,str(horarioAtual.horas))))

    elif (horarioDoPao.segundos >= 60 or horarioDoPao.segundos <= 0
        or horarioDoPao.minutos >= 60 or horarioDoPao.minutos <= 0
            or horarioDoPao.horas >= 24 or horarioDoPao.horas <= 0) :
        raise (ExcecaoTempo('Você digitou o horário do pão inválido: {0}:{1}:{2}'.format(str(horarioDoPao.segundos),
                                                                                   str(horarioDoPao.minutos),
                                                                                   str(horarioDoPao.horas))))

def horarioTermino(horarioAtual,horarioDoPao):
    termino = Horario()
    termino.segundos = horarioAtual.segundos + horarioDoPao.segundos
    termino.minutos = horarioAtual.minutos + horarioDoPao.minutos
    termino.horas = horarioAtual.horas + horarioDoPao.horas

    if (termino.segundos >=60):
        termino.segundos = termino.segundos - 60
        termino.minutos = termino.minutos + 1

    elif (termino.minutos >=60):
        termino.minutos = termino.minutos - 60
        termino.horas = termino.horas + 1
    return termino

horarioAtual = Horario()
horarioDoPao = Horario()

while(1):

    try:
        horarioAtual.segundos = int(input('Digite os segundos: '))
        horarioAtual.minutos =  int(input('Digite os minutos: '))
        horarioAtual.horas = int(input('Digite as horas: '))

        horarioDoPao.segundos = int(input('Digite os segundos do horario do pão: '))
        horarioDoPao.minutos = int(input('Digite os minutos do horario do pão: '))
        horarioDoPao.horas = int(input('Digite as horas do horario do pão: '))
        validacaoHorario(horarioAtual,horarioDoPao)
        break
    except ExcecaoTempo as excecao:
        print(excecao)
        print('Digite novamente os valores do horário atual e do horário do pão!!!')
        continue

termino = horarioTermino(horarioAtual,horarioDoPao)

print('{0}:{1}:{2}'.format(str(termino.segundos),str(termino.minutos),str(termino.horas)))


lista = [1,2,3,4,5,6,7,8,9]
tupla = (0,1,2,3,4,5,6,7,8,9)
dicionario = {0:'a',1:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n'}
