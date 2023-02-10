#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Importar modulo inteiro
import math
valor = float(input('Digite um valor: '))
print('O valor digitado {} e a sua parte inteira é {}'. format(valor, math.trunc(valor)))

#Importar somente uma função
from math import trunc
num = float(input('Digite um número: '))
print('O número digitado foi {}, sua parte inteira é {}'. format(num, trunc(num)))

# Sem importar módulo
num = float(input('Digite um número qualquer: '))
print('A parte inteira do número {} é {}.'.format(num, int(num)))
