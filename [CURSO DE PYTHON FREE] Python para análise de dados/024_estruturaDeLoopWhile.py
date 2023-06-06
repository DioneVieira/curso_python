# LOOP WHILE
"""Python While Loop é usado para executar um bloco de instruções repetidamente até que uma determinada condição seja
satisfeita. E quando a condição se torna falsa, a linha imediatamente após o loop no programa é executada.
While loop se enquadra na categoria de iteração indefinida. A iteração indefinida significa que o número de vezes que
o loop é executado não é especificado explicitamente com antecedência.

while expressão: loop"""
import random

parar = 0
while parar <= 10:
    print(parar)
    parar += 1

print('\n______________________________________________________________________\n')

loop = 0
while loop <= 10:
    print(loop)

    if loop == 5:
        for x in range(10):
            print(random.random())
    loop += 1

print('\n______________________________________________________________________\n')
print('###___JOGO___###')

while True:
    jogador_01 = random.randint(0, 10)
    jogador_02 = random.randint(0, 10)

    print('Jogador 1 tirou: ', jogador_01)
    print('Jogador 2 tirou: ', jogador_02)

    if jogador_01 > jogador_02:
        print('Jogador 1 ganhou!!!')
        break
    print('\n')