#TIPOS DE DADOS
#Esses tipos de dados podem receber qualquer tipo de informação, inclusive Operações Aritiméticas

#1.LISTAS - São criadas usando [](Colchetes)
lista_exemplo01 = [1,2,3,4,5,6]
print(lista_exemplo01)
lista_exemplo02 = ['nome', 'sobrenome', 'idade', 7,8,9]
print(lista_exemplo02)
lista_exemplo03 = [1, 'texto', True, [1,2,3]]
print(lista_exemplo03)

#2.Tuplas - São criadas usando ()(Parenteses) - são imutaveis
tupla_exemplo01 = (1,2,3,4,5,6)
tupla_exemplo02 = ('texto', True, 2, 2.90)
print(tupla_exemplo01, tupla_exemplo02)

#3.Dicionários - São criados usando {}(Chaves)
dicionario = {
    'Index' : 'Valor',
    'Id' : 1,
    'Id' : 2,
    'Nome' : 'Dione',
    'Lista' : lista_exemplo01,
    'Tupla' : tupla_exemplo01
}
print(dicionario)