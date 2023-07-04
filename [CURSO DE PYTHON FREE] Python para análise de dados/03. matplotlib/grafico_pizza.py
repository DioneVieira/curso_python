import matplotlib.pyplot as plt

# Dados para plotar
paises = 'Euro', 'Dólar', 'Libra esterlina', 'Iene'
tamanhos = [4017, 3348, 855, 256]

# definições
colors = ['lightcoral','gold', 'yellowgreen',  'lightskyblue']

# explodir 1ª fatia
explode = (0.1, 0, 0, 0)

# Plot
plt.pie(tamanhos, explode=explode, labels=paises, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()