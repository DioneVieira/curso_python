# 3ª Exercício

"""Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome completo
do usuário na tela."""

nome=input('Digite seu primeiro nome: ').strip().title()
sobrenome=input('Digite seu sobrenome: ').strip().title()
print(f'{nome} {sobrenome}')
