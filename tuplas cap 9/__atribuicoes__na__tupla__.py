
#para trocar valores entre variaveis, e necessario realizar as tres atribuicoes

#troca = a
#a = b
#b = troca

#com o tempo esta abordagem se torna incomoda, em python temos a seguinte notacao:

# a,b = b,a

#o lado esquerdo contem uma tupla de variaveis, enquanto que no lado direito ha uma tupla de valores. cada valor e atribuido
#a sua seguinte variavel

#o numero de variaveis e valores deve ser obrigatoriamente igual


a = 1
b = 2

print('valor de a antes a troca: ',a)
print('valor de b antes a troca: ',b)

a,b = b,a

print('valor de a apos a troca: ',a)
print('valor de b apos a troca: ',b)
