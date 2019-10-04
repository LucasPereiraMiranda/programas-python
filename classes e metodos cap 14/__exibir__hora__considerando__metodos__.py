
#sempre devemos colocar o args

class DataInvalidaException(Exception):
    pass

class Horario:
    def exibirHorario(self,args):
        if((args.segundos > 60 or args.segundos < 0) or (args.minutos > 60 or args.minutos < 0) or (args.horas > 24 or args.horas < 0 )):
            raise DataInvalidaException("Error")
        else:
            print('{0}:{1}:{2}'.format(str(args.segundos),str(args.minutos),str(args.horas)))


tempo = Horario()

tempo.segundos = int(input('Digite os segundos: '))
tempo.minutos = int(input('Digite os minutos: '))
tempo.horas = int(input('Digite as horas: '))

try:
    tempo.exibirHorario(tempo)
except DataInvalidaException as msg:
    print(msg)