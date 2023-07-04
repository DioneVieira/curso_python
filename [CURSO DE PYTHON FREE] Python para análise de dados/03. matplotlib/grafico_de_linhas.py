from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(x, y, 'k--', linewidth=5)
# plt.plot([1, 2, 3], [4, 5, 6], '--', color='#42f5e0', lw=3)

# plt.title("Título esquerdo", fontdict={'family': 'serif', 'color': 'darkblue', 'weight': 'bold', 'size': 14},
# loc='left')
plt.title("Gráfico de linhas", fontdict={'family': 'monospace', 'color': 'blue', 'weight': 'bold', 'size': 15},
          loc='center')
# plt.title("Título direita", fontdict={'family': 'fantasy', 'color': 'black','weight': 'bold', 'size': 16},
# loc='right')
plt.xlabel('Valores do eixo X', family='serif', color='r', weight='normal', size=16, labelpad = 6)
plt.ylabel('Valores do eixo Y', family='serif', color='r', weight='normal', size=16, labelpad = 6)

plt.show()


"""Como alterar a cor da linha em Matplotlib
As cores básicas integradas têm o alias abaixo:

b = blue
g = green
r = red
c = cyan
m = magenta
y = yellow
k = black
w = white

Como mudar estilo de Linha em Matplotlib ?
Matplotlib tem 4 estilos de linha integrados:

"-" Matplotlib Line Chart - Line Style 
"--" Matplotlib Line Chart - Line Style 
":" Matplotlib Line Chart - Line Style"""