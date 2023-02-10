#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi utilizado: '))
km = float(input('Qantos KM foram percorridos com o carro: '))
print('*'*100)
print('O valor total do aluguel a ser pago será de R${:.2f}.'.format((60*dias)+(0.15*km)))