#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang = float(input('Digite o valor do angulo: '))
print('O SENO é: {:.2f}\n O COSSENO é: {:.2f}\n A TANGENTE é: {:.2f}'. format(sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))