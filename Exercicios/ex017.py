#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Qual valor do cateto oposto: '))
ca = float(input('Qual valor do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa mede {:.2f}'. format(hi))