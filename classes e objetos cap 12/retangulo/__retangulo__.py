
class __Retangulo__:
    pass

class __Ponto__:
    pass

box = __Retangulo__()

box.largura = 100.0
box.altura = 200.0

box.bordas = __Ponto__()
box.bordas.x = 0.0
box.bordas.y = 0.0

print(box.bordas.x)
print(box.bordas.y)

