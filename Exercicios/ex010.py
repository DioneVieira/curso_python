#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quantos reais você tem? R$'))
dolar = float(input('Qual a cotação do dólar hoje? US'))
print('='*100)
print('Você pode comprar US{:.2f} dólares com R${:.2f} reais.'. format(real/dolar, real))
print('Euro: EUR{:.2f}'.format(real/5.51))
