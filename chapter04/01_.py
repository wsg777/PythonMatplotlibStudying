# generate shadow for title and labels
# 为标题和标签添加阴影
from matplotlib import pyplot as plt
from matplotlib import patheffects
import numpy as np

# generate 70 standard normal distribution numbers
data = np.random.randn(70)

fontsize = 18
plt.plot(data)

# generate title and axis labels
title = 'This is figure title'
x_label = 'This is x axis label'
y_label = 'This is y axis label'
# plt.title()是生成标题的方法，第一个参数是标题的内容，fontsize指定标题字体大小，verticalalignment用来布置文本
#   值有'top', 'bottom', 'center', 'baseline'，设置成bottom离图表最远
# 这个方法是有返回值的，返回的是标题对象
title_text_obj = plt.title(title, fontsize=fontsize, verticalalignment='bottom')
# 这一行代码用于生成标题阴影
title_text_obj.set_path_effects([patheffects.withSimplePatchShadow()])

# apply them to the xaxis and yaxis labels
xlabel_obj = plt.xlabel(x_label, fontsize=fontsize, alpha=0.5)
ylabel_obj = plt.ylabel(y_label, fontsize=fontsize, alpha=0.5)
xlabel_obj.set_path_effects([patheffects.withSimplePatchShadow(shadow_rgbFace='red')])
ylabel_obj.set_path_effects([patheffects.withSimplePatchShadow(shadow_rgbFace='red')])


plt.savefig('test401.png')
plt.show()
