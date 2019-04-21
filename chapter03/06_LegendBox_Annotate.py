# 图例和注解
from matplotlib import pyplot as plt
import numpy as np

# generate different normal distribute
x1 = np.random.normal(30, 3, 100)
x2 = np.random.normal(20, 2, 100)
x3 = np.random.normal(10, 3, 100)

# plot them
plt.plot(x1, label='plot')
plt.plot(x2, label='plot2')
plt.plot(x3, label='plot3')

# generate a legend box
# bbox_to_anchor参数指定边框，值为一个四元组，四元组的前两个值为起始点的位置，后两个参数为宽度和高度。大于1或小于0的值表示在图表外面。
# loc参数指定起始点是哪一个
# ncol是一行最多显示的列数
# mode参数课设置为None或expand，当为expand时，图例框会水平扩展至整个坐标轴区域
# borderaxespad参数指定坐标轴和图例边界之间的间距
plt.legend(bbox_to_anchor=(0, -0.15, 0.4, 0.02), loc='upper right', ncol=3, mode="expand", borderaxespad=0)

# annotate an important value
# 第一个参数是注解的内容，第二个参数是注解指向的位置
# ycoords='data'指定注解和数据使用相同的坐标系
# xytext参数指定注解显示的位置
# arrowprops参数指定箭头属性
plt.annotate("Important value", (55, 20), xycoords='data', xytext=(5, 38), arrowprops=dict(arrowstyle='->'))

plt.savefig('test306.png')
plt.show()