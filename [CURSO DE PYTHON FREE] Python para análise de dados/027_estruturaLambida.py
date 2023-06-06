#  ESTRUTURA LAMBIDA
"""Uma função lambda é uma pequena função anônima.
Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão."""

funcao_soma = lambda valor: valor + 10

print(funcao_soma(1))

funcao_soma_02 = lambda valor_1, valor_2 : valor_1 + valor_2

print(funcao_soma_02(10, 10))

exemplo = lambda valor : 'Verdadeiro' if valor % 2 == 0 else 'Falso'
print(exemplo(1))

# Função Lambda
Nao_Faxa_isso = lambda Qualquer_Valor: 'Verdadeiro' if Qualquer_Valor % 2 == 0 else 'Falso'
Nao_Faxa_isso = lambda x: True if x % 2 == 0 else False
print(Nao_Faxa_isso( 105 ))