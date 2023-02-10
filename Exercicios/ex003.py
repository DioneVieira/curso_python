# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Enter a value: ')) # indicar valor primitivo( Int, Float)
n2 = int(input('Enter another value: '))

soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divi = n1 / n2

print('Mathematical results between number {} and {} are: Addition: {}; Subtraction: {}; Multiplication: {}; Division: {}. '. format(n1, n2, soma, subt, mult, divi))

