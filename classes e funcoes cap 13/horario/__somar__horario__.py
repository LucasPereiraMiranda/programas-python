
class Horario:
    pass

#funcao pura, pois não modifica os objetos passados como parâmetro
def somaHorario(h1,h2):
    soma = Horario()
    soma.horas = h1.horas + h2.horas
    soma.minutos = h1.minutos + h2.minutos
    soma.segundos = h1.segundos + h2.segundos
    return soma

def exibir(objxibir):
    print('Tempo: {0}:{1}:{2}'.format(str(objxibir.segundos),str(objxibir.minutos),str(objxibir.segundos)))

h1 = Horario()
h2 = Horario()

h1.segundos = 5
h1.minutos = 10
h1.horas = 5

h2.segundos = 10
h2.minutos = 30
h2.horas = 8

tempoSomado = somaHorario(h1,h2)
exibir(tempoSomado)
