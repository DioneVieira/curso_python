#Faça um programa que leia um número INTEIRO e mostre o seu sucessor e antecessor.

n = int(input('Digite um número: '))

print('Você digitou o número {}, o seu antecessor é {}, e o sucessor é {}!'.format(n, (n - 1), (n + 1)))