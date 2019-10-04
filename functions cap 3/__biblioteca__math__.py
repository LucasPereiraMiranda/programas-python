
import math

grau = float(input('digite um valor em graus:  '))
angulo_em_rad = (grau * 2 * math.pi)/360
print(angulo_em_rad)

#caso desejamos determinar o sen do angulo, estando o mesmo em radianos, devemos utilizar esta funcao

print(math.sin(angulo_em_rad))
seno = math.sin(angulo_em_rad)
if seno < 10 :
    print('o sen de {0} e menor do que 10'.format(str(angulo_em_rad)))
else :
    print('o sen de {0} e maior ou igual a 10'.format(str(angulo_em_rad)))
