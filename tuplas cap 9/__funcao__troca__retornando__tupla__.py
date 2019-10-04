
def troca(x,y):
    return (y,x)


x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

print('valor de x antes da troca: ',x)
print('valor de y antes da troca: ',y)

# poderia ser tupla = (x,y) e mostrarmos tupla[0], como sendo x e tupla[1], como sendo y

(x,y) = troca(x,y)

print('valor de x apos a troca: ',x)
print('valor de y apos a troca: ',y)
