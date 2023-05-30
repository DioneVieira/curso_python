#FATIAMENTO DE STRINGS
'''Strings são listas de bytes representando caracteres.
Podemos acessar suas posições usando Colchetes
String[Posição Inicial: Posição Final]'''

minha_string = 'Aprender Python é top!'
cpf ='CPF:123456789'
print(type(minha_string))
print(len(minha_string))
print(minha_string[0])
print(minha_string[2])
print(minha_string[-1])
print(minha_string[-10:])
print(minha_string[0:8])
print(cpf[-9:])