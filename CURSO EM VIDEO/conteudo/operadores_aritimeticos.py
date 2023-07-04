valor_1 = int(input('1º valor: '))
valor_2 = int(input('2º valor: '))
valor_3 = int(input('3° valor: '))
valor_4 = int(input('4° valor: '))

print('A soma entre o 1º e o 2º é {}. '.format(valor_1 + valor_2)) #ADIÇÃO
print('A subtração entre o 4º e o 2° é {}. '.format(valor_4 - valor_2)) #SUBTRAÇÃO
print('A divisão entre o 3º e o 1° é {}.'.format(valor_3 / valor_1)) #DIVISÃO
print('A divisão inteira entre o 1º e o 4° é {}.'.format(valor_1 // valor_2)) #DIVISÃO INTEIRA
print('A multiplicação entre o 3º e o 2º é {}.'.format(valor_3 * valor_2)) #MULTIPLICAÇÃO
print('O resto da divisão entre o 1º e o 2º é {}.'.format(valor_1 % valor_2)) #RESTO DA DIVISÃO
print('A potênciação entre o 3º e o 4º é {}.'.format(valor_1 ** valor_2)) #POTÊNCIA
print('='*100)
print(valor_1 + valor_2 * valor_3)
print(valor_2 * valor_1 + valor_4 ** valor_3)
print(valor_2 * (valor_1 + valor_4) ** valor_3)
print('='*100)
x = (10 + 5) * 4
y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(x)
print(y)