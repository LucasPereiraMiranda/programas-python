

class Time:

    def incrementar(self,t1):
        t1.segundos = t1.segundos + 1

        while t1.segundos >= 60:
            t1.segundos = t1.segundos - 60
            t1.minutos = t1.minutos + 1

        while t1.minutos >= 60:
            t1.minutos = t1.minutos - 60
            t1.horas = t1.horas + 1

    def exibir(self,t1):
        print('{0}:{1}:{2}'.format(str(t1.segundos),str(t1.minutos),str(t1.horas)))


t1 = Time()

t1.segundos = 80
t1.minutos = 10
t1.horas = 15

t1.incrementar(t1)
t1.exibir(t1)