# 散点图
from matplotlib import pyplot as plt
import numpy as np

# generate x values (standard normal distribution)
x = np.random.randn(1000)

# random measurements, no correlation
y1 = np.random.randn(len(x))
# strong correlation
y2 = 1.2 + np.exp(x)

ax1 = plt.subplot(121)
plt.scatter(x, y1, color='indigo', alpha=0.3, edgecolors='white', label='no correl')
plt.xlabel('no correlation')
plt.grid(True)
plt.legend()

plt.ylim(-5, 30)

ax2 = plt.subplot(122)
plt.scatter(x, y2, color='green', alpha=0.3, edgecolors='grey', label='correl')
plt.xlabel('strong correlation')
plt.grid(True)
plt.legend()

plt.ylim(-5, 30)

plt.savefig('test312.png')
plt.show()

