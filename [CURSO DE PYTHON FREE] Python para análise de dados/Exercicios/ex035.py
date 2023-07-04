# 35ª Exercício

"""Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário.
Utilize como referência as informações a seguir. Caso o usuário não digite uma categoria válida (número entre 1 e 10)
mostre uma mensagem personalizada na tela."""


categoria=int(input('Digite a categoria do produto (1 até 10): '))
if categoria==1:
    print('O preço do produto é: $ 0.5')
elif categoria==2:
    print('O preço do produto é: $ 11.3')
elif categoria==3:
    print('O preço do produto é: $ 17.5')
elif categoria==4:
    print('O preço do produto é: $ 33.97')
elif categoria==5:
    print('O preço do produto é: $ 103.47')
elif categoria==6:
    print('O preço do produto é: $ 44.67')
elif categoria==7:
    print('O preço do produto é: $ 12.55')
elif categoria==8:
    print('O preço do produto é: $ 14.87')
elif categoria==9:
    print('O preço do produto é: $ 98.12')
elif categoria==10:
    print('O preço do produto é: $ 131.4')
else:
    print('Opção inválida.')
