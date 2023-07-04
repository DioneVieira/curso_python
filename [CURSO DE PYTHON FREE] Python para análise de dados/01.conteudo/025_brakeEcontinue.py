#  BREAK e CONTINUE

"""O uso de loops no Python automatiza e repete as tarefas de maneira eficiente. Mas, às vezes, pode surgir uma condição
em que você deseja sair completamente do loop, pular uma iteração ou ignorar essa condição. Isso pode ser feito por
instruções de controle de loop. As instruções de controle de loop alteram a execução de sua sequência normal.
Quando a execução sai de um escopo, todos os objetos automáticos criados nesse escopo são destruídos.
Python suporta as seguintes instruções de controle."""

lista = ['Morango', 'Pera', 'Uva', 'Abacaxi']

for fruta in lista:
    print(fruta)
    if fruta == 'Uva':
        break

print('\n')

for loop in range(0,11):
    if loop == 5:
        continue
        print('Cheguei aqui mas não vou mostrar o numero 5')

    print(loop)

print('\n')

# For + Lista + IF + Break
Lista_Paises = ['Brasil', 'Argentina', 'Uruguai', 'Chile', 'Paraguai', 'Bolivia',
                'Equador', 'Colombia', 'Suriname, Guiane, Goianai France']
Loop = 0

for P in Lista_Paises:

  if P == 'Chile':
    print('Chegou')
    break

  else:
    pass

  Loop += 1
  print( Loop )

print('\n')

# While
Loop = 0

while Loop <= 10:
    print(Loop)
    Loop += 1

    if Loop == 5:

        for c in range(10):
            print(c)

        break

print('\n')

# Loop de 1 a 10
for i in range(1, 11):

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 5:
        print(f'{i}º interação --> Estou no IF')
        continue

    else:
        # otherwise print the value
        # of i
        print(f'{i}º Continue continua sempre!!!!')
        # print(i)