#  FUNÇÃO
"""Uma função é um bloco de código que só é executado quando é chamado.
As funções são úteis para organizar o código em blocos reutilizáveis e modulares. Você pode definir uma função uma vez
e chamá-la várias vezes em diferentes partes do programa. Isso ajuda a evitar a repetição de código e torna o programa
mais organizado e legível.
Você pode passar dados, conhecidos como parâmetros, para uma função.
Uma função pode retornar dados como resultado."""


def boas_vindas():
    print('*******.Hello World.*******')


boas_vindas()

print('Soma')
def Somar(Valor1, Valor2):
    Soma = Valor1 + Valor2
    print(Soma)


for loop in range(0, 10):
    import random

    x = random.random()
    y = random.random()

    Somar(x, y)

print('\n')

print('Somar com entrada de valores (input)')
def Somar():
    Valor1 = float(input("Digite o Valor1: "))
    Valor2 = float(input("Digite o Valor2: "))
    Soma = Valor1 + Valor2
    print(Soma)


Somar()

from random import randint
# Função
def Sobrenome( Algum_Texto, Numero ):
  print(f'Nome dele é: {Algum_Texto}')

  if Numero >= 10:
    print('Maior que 10')
  else:
    print('NADA!')

Lista_Nomes = ['Odemir', 'Luigi', 'Mariana']

for Nome in Lista_Nomes:
  Sobrenome( Nome, randint(1,12) )
