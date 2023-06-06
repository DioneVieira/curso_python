# CONDIÇÃO IF
"""if é a declaração mais simples de tomada de decisão.
Ele é usado para decidir se uma determinada instrução ou bloco de instruções será executado, ou não, ou seja, se uma
determinada condição for verdadeira, um bloco de instruções será executado, caso contrário, não.

if condição:
declarações a serem executadas se
condição é verdadeira"""

# 1- Condição se a pessoa tiver menos de 18 anos, ela não pode tirar carteira de motorista.

idade = int(input('Qual sua idade: '))
if idade >= 18:
    print('Você é maior de idade, pode tirar sua carteira de motorista!')
elif idade == 17:
    print('Você pode dar entrada no seu processo para tirar sua carteira de motorista, mas só pode dirigir com 18 anos!')
else:
    print('Você é menor de idade, ainda não pode tirar sua carteira de !')
