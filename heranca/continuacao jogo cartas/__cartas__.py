
import random

class Carta:
    lista_de_naipes = ("Paus","Ouros","Copas","Espadas")
    lista_de_posicoes = ("Narf","Ás","2","3","4","5","6","7","8","9","10","Valete","Dama","Rei")

    # metodo construtor
    def __init__(self,naipe,posicao):
        self.naipe = naipe
        self.posicao = posicao

    #metodo str, analogo ao toString em java
    def __str__(self):
        return (self.lista_de_posicoes[self.posicao] + " de " + self.lista_de_naipes[self.naipe])

    #metodo cmp, analogo ao equals em java

    def __cmp__(self,other):
        #verificar os nipes
        if self.naipe > other.naipe:
            return 1
        elif self.naipe < other.naipe:
            return -1
        #analisando agora a posicao das cartas
        if self.posicao > other.posicao:
            return 1
        elif self.posicao < other.posicao:
            return -1
        #caso forem iguais, retorna-se 0
        return 0

class Baralho:
    cartas = []
    def __init__(self):
        for naipe in range(0,4):
            for posicao in range (1,14):
                self.cartas.append(Carta(naipe,posicao))


    def __str__(self,baralho):
        print("Cartas contidas no baralho: ")
        for obj in baralho.cartas:
            if(obj != None):
                print(obj)
            else:
                continue

    def embaralhar(self):
        n_cartas = len(self.cartas)
        for i in range(0,n_cartas):
            j = random.randrange(i,n_cartas)
            self.cartas[i],self.cartas[j] = self.cartas[j],self.cartas[i]

    def remover_cartas(self,carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            return 1
        else:
            return 0

    def obter_carta_topo(self):
        return self.cartas.pop()

    def verifica_baralho_vazio(self):
        if len(self.cartas)==0:
            return 1
        else:
            return 0

    def distribuir_cartas(self,maos,n_cartas = 999):
        n_maos = len(maos)
        for i in range(0,n_cartas):
            if self.verifica_baralho_vazio():
                break                           #interromper, caso acabarem as cartaas
            else:
                carta = self.obter_carta_topo()#pegar a carta do topo (pop)
                mao = maos[i % n_maos]          #quem deve receber a carta agora?
                mao.adicionar_carta(carta)      #adicionar a carta a mao



class Mao(Baralho): #na heranca em python, a classe mae fica entre parenteses

    def __init__(self,nome=""):
        self.cartas = []
        self.nome = nome

    def adicionar_carta(self,carta):
        self.cartas.append(carta)

    def __str__(self,mao):
        print('\nCartas contidas na mão do',mao.nome)
        for obj in mao.cartas:
            print(obj)

class JogoDeCartas:

    def init__(self):
        self.baralho = Baralho()
        self.baralho.embaralhar()


class MaoDeMico(Mao):

    def descartar_casais(self):
        conta = 0
        cartas_iniciais = self.cartas[:]
        for carta in cartas_iniciais:
            casal = Carta(3 - carta.naipe,carta.valor)
            if casal in self.cartas:
                self.cartas.remove(carta)
                self.cartas.remove(casal)
            print("Mao %s:%s casais %s" % (self.nome,carta,casal))
            conta = conta + 1
        return conta

print("\n             Seja bem-vindo ao jogo de cartas\n")

jogo = JogoDeCartas()
mao = MaoDeMico("Lucas")
jogo.baralho.distribuir_cartas([mao],13)
print(mao.__str__(mao))

"""
print("\nObtendo o baralho...")
baralho = Baralho()
print("Embaralhando o baralho...\n")
baralho.embaralhar()
mao = Mao('Lucas')
mao2 = Mao('Pedro')
baralho.distribuir_cartas([mao,mao2], 6)
print(mao.__str__(mao))
print(mao2.__str__(mao2))
"""
