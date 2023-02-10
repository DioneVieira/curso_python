#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Qual a temperatura em Celsius? '))
f = ((c*9)/5)+32
k = (c+273.15)
print('-'*100)
print('A temperatura em Fahrenheit é de {:.1f}°F.'.format(f))
print('A temperatura em Kelvin é de {:.2f}K.'.format(k))