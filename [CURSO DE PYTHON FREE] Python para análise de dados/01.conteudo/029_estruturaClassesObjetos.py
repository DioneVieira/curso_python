# ESTRUCTURA DE CLASSES/OBJETOS
"""Python é uma linguagem de programação orientada a objetos.
Quase tudo em Python é um objeto, com suas propriedades e métodos.
Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos"""

class Pessoa:

    # Metodo Construtor
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_Vindas(self):
        print('Olá seja bem vindo ', self.Nome.upper(),'!!!')

    def Recusado(self):
        print('Seu acesso foi recusado!')

    #Função
    def Maior_Idade(self):
        if self.Idade >= 18:
            print('Usuário maior de idade!')
            self.Boas_Vindas()
        else:
            print('Usuário menor de idade!!!')
            self.Recusado()

Dados = Pessoa('Dione', 30)

Dados.Maior_Idade()

print('------------------------------------------------------------')

class Pessoa:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_Vindas(self):
        print('Olá, seja bem-vindo', self.Nome.upper(),'!!!')

    def Recusado(self):
        print('Seu acesso foi recusado!')

    def Maior_Idade(self):
        if self.Idade >= 18:
            print('Usuário maior de idade!')
            self.Boas_Vindas()
        else:
            print('Usuário menor de idade!!!')
            self.Recusado()

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

Dados = Pessoa(nome, idade)
Dados.Maior_Idade()

print('_' * 200)

class Pessoa:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_Vindas(self):
        print('Olá, seja bem-vindo', self.Nome.upper(),'!!!')

    def Recusado(self):
        print('Seu acesso foi recusado!')

    def Maior_Idade(self):
        if self.Idade >= 18:
            print('Usuário maior de idade!')
            self.Boas_Vindas()
        else:
            print('Usuário menor de idade!!!')
            self.Recusado()

    @staticmethod
    def obter_dados_pessoa():
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        return nome, idade


nome, idade = Pessoa.obter_dados_pessoa()
dados = Pessoa(nome, idade)
dados.Maior_Idade()
