#  ESTRUTURA TRY
"""O try permite testar um bloco de código quanto a erros.
O except permite que você lide com o erro.
O else permite executar código quando não há erro.
O finally permite que você execute código, independentemente do resultado dos blocos try e except."""

try:
    0 / 0
    print('Deu certo meu script!!!')

except:
    print('Não deu certo!!!')

finally:
    print('Vou ser excutado da msm forma!!!')

print('\n')

try:
  print(Algo_Coisa_Que_Nao_Defini)

except NameError:
  print("Ops deu algum erro!")

finally:
  print("Vou ser executado de qualquer forma")

print('\n')

try:
    numero = int(input("Digite um número inteiro: "))
    print("O número digitado foi:", numero)

except ValueError:
    print("Erro: você deve digitar um número inteiro!")

finally:
    print("O bloco 'finally' será executado de qualquer forma.")