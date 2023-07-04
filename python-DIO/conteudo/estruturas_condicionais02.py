'''
import sys


opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe o valor para saque: "))

elif opcao == 2:
    print("Exibindo extrato...")
else:
    sys.exit('Opção inválida')
'''
#################################################################

MAIOR_IDADE = 18

idade = int(input('Informe a sua idade: '))
if idade >= MAIOR_IDADE:
    print("Você tem", idade,'anos. Você pode tirar CHN.')

elif idade >=17:
    print("Você tem ", idade, "anos. Com 17 anos você pode fazer as aulas teóricas para tirar CNH.\nSomente com 18 você pode fazer as aulas praticas.")

else:
    print("Você tem ", idade, "anos. É menor de idade, não pode tirar CNH>")
