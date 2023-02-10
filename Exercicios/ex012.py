#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual  o valor do produto? R$ '))
valor = (preço - (preço*5/100))
print('O valor do produto com 5% de desconto é R$ {:.2f}'.format(valor))