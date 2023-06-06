# LAÇO FOR
"""O loop For do Python é usado para travessia sequencial, ou seja, é usado para iterar sobre um iterável como string,
tupla, lista, etc. Ele se enquadra na categoria de iteração definida. Iterações definidas significam que o número de
 repetições é especificado explicitamente com antecedência.
for variável in objeto: loop"""

for x in range(11):
    print(x * 5)

print('\nIdentifica onde começar o loop ex = 1.')
for x in range(1, 11):
    print(x * 5)

print('\nConta a partir de um valor especifica ex = a cada 5.')
for x in range(1, 100, 5):
    print(x)

print('\n______________________________________________________________________\n')

lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Bolivia', 'Colombia', 'Equador']
for paises in lista:
    print('Abreviação do país ' + paises + ' = ', paises.upper()[0:3])

print('\n______________________________________________________________________\n')

lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Bolivia', 'Colombia', 'Equador']
for paises in lista:
    if paises == 'Brasil':
        print(paises, 'é Penta')

        for y in range(10):
            print(y)

print('\n______________________________________________________________________\n')

for loop in range(0, len(lista), 2):
    print(lista[loop])

for ordem, paises in enumerate(lista):
    print(ordem, paises)

print('\n______________________________________________________________________\n')
Lista = [numero for numero in range(0, 10)]
print(Lista)

Lista = []
for loop in range(0, 10):
    Lista.append(loop)
print(Lista)


print('\n______________________________________________________________________\n')

nomes = ["Alice", "Bob", "Charlie"]

for nome in nomes:
    print("Olá, " + nome + "!")

print("Fim do programa")
