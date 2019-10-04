
#procedimento sem retorno
def nome_da_funcao(nome, cargo):
    print('Seu nome é: {0}'.format(str(nome)))
    print('Seu cargo é: {0}'.format(str(cargo)))


def nome_da_funcao2(endereco):
    print('Seu endereço é: {0}'.format(str(endereco)))

def nome_da_funcao3():
    print('Cadastrado com sucesso!')

nome = input('Digite o seu nome:  ')
cargo = input('Digite o seu cargo:  ')
endereco = input('Digite o seu endereço: ')
nome_da_funcao(nome,cargo)
nome_da_funcao2(endereco)
nome_da_funcao3()

