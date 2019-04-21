# use subplots
# 使用子区

import matplotlib.pyplot as plt

plt.figure(0)
axes1 = plt.subplot2grid((3,3), (0, 0), colspan=3)
axes2 = plt.subplot2grid((3,3), (1, 0), colspan=2)
axes3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
axes4 = plt.subplot2grid((3,3), (2, 0))
axes5 = plt.subplot2grid((3,3), (2, 1))

plt.subplots_adjust(wspace=1, hspace=1)

axes1.set_title("This is title1")
axes2.set_title("This is title2")
axes3.set_title("This is title3")
axes4.set_title("This is title4")
axes5.set_title("This is title5")

all_axes = plt.gcf().axes
for ax in all_axes:
    for ticklabel in ax.get_xticklabels() + ax.get_yticklabels():
        ticklabel.set_fontsize(10)

plt.suptitle("This is subtitle")

plt.savefig('test402.png')
plt.show()
