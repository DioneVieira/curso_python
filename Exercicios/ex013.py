#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
atual = float(input('Qual é o salario atual do funcionário? R$ '))
aumento = float(input('Quantos porcento ele irá receber de aumento? '))
print('='*100)
print('Parabéns seu novo salario é R$ {:.2f}. Você recebeu {}% de aumento'.format((atual*aumento/100)+atual, aumento))