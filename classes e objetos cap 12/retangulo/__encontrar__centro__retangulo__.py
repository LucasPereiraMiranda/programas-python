class __Retangulo__:
    pass

class __Ponto__:
    pass

#vamos retornar um ponto referente ao centro do retangulo
def encontrarCentro(box):
    pontoRetorno = __Ponto__()
    pontoRetorno.x = box.bordas.x + box.largura/2.0
    pontoRetorno.y = box.bordas.y + box.altura/2.0
    return pontoRetorno

box = __Retangulo__()
box.largura = 100.0
box.altura = 200.0
box.bordas = __Ponto__()
box.bordas.x = 0.0
box.bordas.y = 0.0
centro = encontrarCentro(box)
print('Cordenada do centro do retangulo: ({0},{1})'.format(str(centro.x),str(centro.y)))
