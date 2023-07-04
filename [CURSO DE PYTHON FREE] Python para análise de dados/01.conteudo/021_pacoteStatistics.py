import statistics
# Este módulo fornece funções para calcular estatísticas matemáticas de dados numéricos e interage com as listas

lista = [12, 15, 28, 31, 56, 78, 78, 80]

print(sum(lista) / len(lista))
# 1- Média
print(statistics.mean(lista))
# 2- Mediana
print(statistics.median(lista))
# Moda
print(statistics.mode(lista))