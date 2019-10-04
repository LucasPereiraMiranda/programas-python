
class Horario:
    pass


def incrementarTempo(tempo):
    tempo.segundos = tempo.segundos + 1

    while tempo.segundos >= 60:
        tempo.segundos = tempo.segundos - 60
        tempo.minutos = tempo.minutos + 1

    while tempo.minutos >= 60:
        tempo.minutos = tempo.minutos - 60
        tempo.horas = tempo.horas + 1

    return tempo

t1 = Horario()

t1.horas = 5
t1.minutos = 10
t1.segundos = 59

incrementarTempo(t1)


print('{0}:{1}:{2}'.format(str(t1.segundos),str(t1.minutos),str(t1.horas)))





