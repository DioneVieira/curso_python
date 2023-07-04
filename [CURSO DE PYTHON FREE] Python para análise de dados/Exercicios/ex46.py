# 46ª Exercício

"""Utilizando estruturas de repetição escreva um programa que mostre os resultados da tabuada (multiplicação) de um
número inserido pelo usuário."""


valor = int(input('Tabuada:'))
for num in range(1, 11):
    print(f'{valor} x {num} = {valor*num}')
