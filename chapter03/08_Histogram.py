# 直方图
from matplotlib import pyplot as plt
import numpy as np

mu = 100
sigma = 20
x = np.random.normal(mu, sigma, 10000000)
ax = plt.gca()

ax.hist(x, bins=100, facecolor='yellow', edgecolor='blue', normed=True)

ax.locator_params('x', nbins = 10)
ax.locator_params('y', nbins = 25)

ax.set_xlabel('Values')
ax.set_ylabel('Frequency')

ax.set_title(r'Normal Distribution ($\mu$=' + str(mu) + ', $\sigma$=' + str(sigma) + ')')
plt.savefig('test308.png')
plt.show()




