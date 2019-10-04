
class Horario:
    pass

def verificacaoSegundos(tempo):
    if tempo.segundos >= 60:
        tempo.segundos = tempo.segundos - 60
        tempo.minutos = tempo.minutos + 1

def verificacaoMinutos(tempo):
    if tempo.minutos >= 60:
        tempo.minutos = tempo.minutos - 60
        tempo.horas = tempo.horas + 1

def incrementar(t1):
    t1.segundos = t1.segundos + 1

def analisarHorario(t1):
    if (t1.segundos < 60 and t1.minutos < 60):
        return
    else:
        verificacaoSegundos(t1)
        verificacaoMinutos(t1)
        analisarHorario(t1)

t1 = Horario()

t1.segundos = 110
t1.minutos = 45
t1.horas = 12
incrementar(t1)
analisarHorario(t1)

print('{0}:{1}:{2}'.format(str(t1.segundos),str(t1.minutos),str(t1.horas)))