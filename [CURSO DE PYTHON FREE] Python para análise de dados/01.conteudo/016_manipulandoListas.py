#MANIPULANDO LISTAS
'''As listas são usadas para armazenar vários itens em uma única variável.
As listas são um dos 4 tipos de dados internos do Python usados para armazenar coleções de dados, os outros 3 são Tuple,
 Set e Dictionary, todos com qualidades e usos diferentes.
Comandos mais utilizados:'''

lista_vazia = []
print(lista_vazia)

print('1- append() - Para adicionar um item ao final da lista',)
lista_vazia.append( 1 )
lista_vazia.append( 2 )
lista_vazia.append( 3 )
lista_vazia.append('valor')
print(lista_vazia)

print('\n2- len() - Calcular o tamanho da lista')
print(len(lista_vazia))

print('\n3- [ ] - Acessar posições (primeira posição é 0)')
print(lista_vazia[0])
print(lista_vazia[-1])
print(lista_vazia[0:2])

print('\n4- del() - Exlcuir um elemento')
print(lista_vazia)
del lista_vazia [3]
print(lista_vazia)

print('\n5- clear() - Limpar a lista')
print(lista_vazia)
lista_vazia.clear()
print(lista_vazia)

lista_vazia_02 = [1, 2, 3, 'valor']
print(lista_vazia_02)

print('\n6- insert() - Para inserir um item de lista em um índice especificado')
lista_vazia_02.insert(4, 'hello')
lista_vazia_02.insert(3, 4)
print(lista_vazia_02)

print('\n7- extend() - Anexar elementos de outra lista à lista atual')
lista_01 = [1, 2, 3]
lista_02 = [4, 5, 6]
lista_01.extend( lista_02)
print(lista_01)

print('\n8- remove() - Remove o item especificado')
lista_01.remove(5)

print('\n9- pop() - Remove o índice especificado')
lista_01.pop(1)
print(lista_01)

print('\n10- sort() - Ordenar os valores')
lista_ABC = ['z', 'c', 'f', 'H', 'A']
lista_ABC.sort()
print(lista_ABC)
lista_ABC.sort(reverse=True)
print(lista_ABC)

print('\n11- copy() - Faz uma copia da Lista')
lista_nova = lista_ABC.copy()
print(lista_nova)

print('\n12- index() - Retorna o index do elemento da lista')
print(lista_nova.index('H'))
