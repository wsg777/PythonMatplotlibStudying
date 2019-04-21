# 误差条形图
import matplotlib.pyplot as plt
import numpy as np

# generate number measurements
x = np.arange(1, 10, 1)

# values computed from "measured
y = np.log(x)
# add some error samples from standard normal distribution
xe = 0.1 * np.abs(np.random.randn(len(y)))
print(y)
print(xe)

# draw and show errorBar
plt.bar(x, y, yerr=xe, width=0.4, align='center', ecolor='r', color='#bbffee', hatch='o', label='experiment #1')

# give some explanations
plt.xlabel('# measurement')
plt.ylabel('Measured values')
plt.title('Measurements')
plt.legend(loc='upper left')


plt.savefig('test309.png')
plt.show()