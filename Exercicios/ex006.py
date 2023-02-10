# Crie um algoritimo que leia um número e mostre o seu dorbro, triplo e a raiz quadrada
n = int(input('Digite um número: '))

print('O número q você digitou foi {}.\nO dobro desse número é {}.\nO triplo é {}.\nE a raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
