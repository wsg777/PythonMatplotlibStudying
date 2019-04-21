# 演示修改线的属性、标题、坐标轴
from matplotlib import pyplot as plt
import numpy as np

# generate data
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

y = np.cos(x)
y1 = np.sin(x)

# plot sin and cos
plt.plot(x, y, linewidth=5, color='green', alpha=0.2, linestyle='--')
plt.plot(x, y1, marker='o', markeredgecolor='red')

# define title
# &&中是斜体
plt.title("Function $sin$ and $cos$", color='brown')

# set x and y limit
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.0, 1.0)
# 如果这里指定的变量范围与下面指定的坐标轴范围不同，会按较大范围呈现

# form ticks at specific values
# \pi表示希腊字母π
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           ['$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'])
plt.yticks([-1, -0.5, 0, 0.5, 1], ['$-1$', '$-0.5$', '$0$', '$0.5$', '$1$'])

plt.savefig('test303.png')
plt.show()
