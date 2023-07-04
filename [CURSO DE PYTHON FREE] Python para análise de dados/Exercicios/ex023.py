# 23ª Exercício

"""Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela
deverá seguir o seguinte formato:

"O número [número] é [par/ímpar]"."""

num=int(input('Número inteiro: '))
if num%2==0:
    print(f'O número {num} é par.')
else:
    print(f'O número é {num} é ímpar.')
