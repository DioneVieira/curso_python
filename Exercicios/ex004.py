#Dissecando uma Variável
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('Digite alguma coisa? ')
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Esta em maiúscula?', algo.isupper())
print('Esta em minúscula?', algo.islower())
print('Esta capitalisada?', algo.istitle())
print('Você digitou {}. Seu tipo é uma {}, ele é um numero = {}, ele é alfabético = {}.'.format(algo, type(algo), algo.isnumeric(), algo.isalpha()))
