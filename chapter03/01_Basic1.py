from matplotlib import pyplot as plt
a = [1, 2, 3, 2, 3, 2, 2, 1]
plt.plot(a)
ax = plt.gca()
plt.title('This is also title')
ax.set_title('This is title')
plt.savefig('test301.png')
plt.show()