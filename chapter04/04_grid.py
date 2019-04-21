# 定制化网格
import matplotlib.pyplot as plt
import numpy as np

# generate standard normal distribution numbers
a = np.random.randn(7)



plt.plot(a)
plt.grid(color='g', linestyle='-', alpha=0.3, linewidth=0.5)

plt.savefig('test404.png')
plt.show()