# 26ª Exercício

# Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.

num=float(input('Digite um número: '))
if num>0:
    print('Número positivo.')
elif num==0:
    print('Número nulo.')
else:
    print('Número negativo.')
