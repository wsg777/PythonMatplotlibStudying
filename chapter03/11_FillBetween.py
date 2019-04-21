# 填充区域
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
y1 = np.sin(x+np.pi/4)
y2 = np.cos(2*x)

# plt.plot(x, y1)
# plt.plot(x, y2)

plt.fill_between(x, y1, y2, facecolor='pink', alpha=0.8, where=y1>=y2)
plt.fill_between(x, y1, y2, facecolor='green', alpha=0.8, where=y1<=y2)

plt.savefig('test311.png')
plt.show()