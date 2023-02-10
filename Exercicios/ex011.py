#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('Calculadora de pintura parede.')
print('='*100)
alt = float(input('Qual é a ALTURA da parede em metros: '))
lar = float(input('Qual é a LARGURA da parede em metros: '))
res = ((alt*lar)/2)
print('='*100)
print('O metro quadrado da sua parede é {:.2f}m².\nCada litro de tinta pinta 2m² de parede.\nVocê vai precisar de {:.2f}L de tinta.'.format(alt*lar,res))