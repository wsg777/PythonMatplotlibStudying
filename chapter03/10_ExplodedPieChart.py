# 分裂式饼图
from pylab import *

# make a square figure and axes
figure(1, figsize=(6, 6))
ax = axes(([0.1, 0.1, 0.8, 0.8]))

# the slices will be ordered and plotted counter-clockwise
labels = ('Spring', 'Summer', 'Autumn', 'Winter')
print(labels)

# fraction are either x/sum(x) or x if sum(x) <= 1
x = [20, 10, 15, 12]

# explode must be len(x) sequence or None
explode = (0.1, 0.1, 0.1, 0.1)

pie(x, explode=explode, labels=labels, autopct='%.2f%%', startangle=67)

rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
title(u'Rainy days by season（数据是瞎编的）')
savefig('test310.png')
show()