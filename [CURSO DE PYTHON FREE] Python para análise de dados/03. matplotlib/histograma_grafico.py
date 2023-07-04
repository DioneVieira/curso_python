import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10**7)
mu = 121
sigma = 21
x = mu + sigma * np.random.randn(1000)

num_bins = 100

n, bins, patches = plt.hist(x, num_bins, density=1, color='blue', alpha = 0.7)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

plt.plot(bins, y, '--', color='black')

plt.xlabel('eixo X')
plt.ylabel('eixo Y')

plt.title('Histograma Matplotlib', fontweight="bold")

plt.show()