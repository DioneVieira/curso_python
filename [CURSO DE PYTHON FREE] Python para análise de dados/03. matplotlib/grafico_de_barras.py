import matplotlib.pyplot as plt

x = ['Python', 'C#', 'C++', 'JavaScript', 'PHP', 'Swif', 'Java']
y = [66, 59, 43, 58, 37, 59, 44]

# plt.plot(x, y, "r--")
plt.bar(x, y, align='center', alpha=0.5)

plt.title("Gráfico de Barras", fontdict={'family': 'monospace', 'color': 'red', 'weight': 'bold', 'size': 16},
          loc='center')

plt.xlabel('Linguagens de programação')
plt.ylabel('Pontuações')

plt.show()