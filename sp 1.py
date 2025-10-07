import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

mu = 170       # rata-rata populasi
sigma = 10     # standar deviasi populasi
n = 30         # ukuran sampel
k = 1000       # jumlah sampel

means = [np.mean(np.random.normal(mu, sigma, n)) for _ in range(k)]

plt.hist(means, bins=30, edgecolor='black', density=True)
plt.title("Distribusi Sampling Rata-rata")
plt.xlabel("Rata-rata Sampel")
plt.ylabel("Frekuensi")
plt.show()
