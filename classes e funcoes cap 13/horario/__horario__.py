

class Horario:
    pass


def imprimeHoras(horario):
    print('Horario: {0}:{1}:{2}'.format(str(horario.segundos),str(horario.minutos),str(horario.horas)))

horario = Horario()
horario.segundos = 5
horario.minutos = 3
horario.horas = 13

imprimeHoras(horario)



