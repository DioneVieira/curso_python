#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A orde de apresentação será: ')
print(lista)

from random import shuffle
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(lista)