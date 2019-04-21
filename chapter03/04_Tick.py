# 刻度
from pylab import *

# get current axis
ax = gca()

# 设置坐标轴平分为几份
ax.locator_params('x', nbins = 10)
ax.locator_params('y', nbins = 25)

# 设置主定位器
# ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(6))

# 正态分布，参数为均值，方差，数量
num = np.random.normal(10, .1, 100)
print(num)
ax.plot(num)
savefig('test304.png')
show()




