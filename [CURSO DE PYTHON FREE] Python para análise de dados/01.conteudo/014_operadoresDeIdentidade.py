#OPERADORES DE INDENTIDADE
'''Os operadores de identidade são usados para comparar os objetos, não se forem iguais, mas se forem realmente o
mesmo objeto, com a mesma localização de memória:'''

#1- is (Retorna True se ambas as variáveis forem o mesmo objeto)
fruta_01 = 'Laranja'
fruta_02 = 'Laranja'
print(type(fruta_01) is type(fruta_02))

#2- is not (Retorna True se ambas as variáveis não forem o mesmo objeto)
fruta_03 = 'Limão'
print(type(fruta_01) is not type(fruta_03))
print(fruta_03 is not fruta_02)