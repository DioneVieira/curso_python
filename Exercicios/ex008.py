#Escreva um programa que leia um valor em metros e o exiba covertido em centimetros e milímetros.

m = float(input('Digite a medida em metros: '))

print('Quilometros: {:.2f}km;\nCentímetros: {:.2f}cm;\nMilímetros: {:.2F}mm,\nPolegadas: {:.2f}"'.format((m/1000),(m*100),(m*1000),(m*39.37)))