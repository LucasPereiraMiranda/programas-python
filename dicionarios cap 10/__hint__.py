#No codigo do fibonacci, muitas recurssoes foram usadas muitas vezes...tornando o processo ineficiente
#Podemos guardar as recurssoes ja utilizadas em uma lista, evitando a repeticao de recurssoes
#Esse processo se chama hint

previo = {0:1,1:1}

def fibonacci(n):
    if(previo.keys().__contains__(n)):
        return previo[n]
    else:
        newValor = fibonacci(n-1) + fibonacci(n-2)
        previo[n] = newValor
        return newValor

num = int(input('Digite um numero inteiro: '))
print('o fibonacci de {0} é: {1}'.format(str(num),str(fibonacci(num))))

#Com esse metodo usando dicionarios, podemos calcular fibonacci de 40 rapidamente, mas podemos ter problemas com
#int overflow apos 50

