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


    def __str__(self):
        for obj in baralho.cartas:
            print(obj)


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

    def distribuir_cartas(self):
        return self.cartas.pop()

    def verifica_baralho_vazio(self):
        if len(self.cartas)==0:
            return 1
        else:
            return 0


    class Jogador:
        cartas_atuais = []

        def receber_cartas(self,carta):
            self.cartas_atuais.append(carta)



print("             Seja bem-vindo ao jogo de cartas\n")
n_jogadores = input("Digite o numero de jogadores: ")
print("Obtendo o baralho...")
baralho = Baralho()
print("Embaralhando o baralho...")
baralho.embaralhar()
print('-------------------------------------------------------------')
print(baralho.__str__())

