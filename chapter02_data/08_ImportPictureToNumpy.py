# 存在问题
import numpy
from PIL import Image
import matplotlib.pyplot as plt

bug = Image.open('stinkbug.png')
arr = numpy.array(bug.getdata(), numpy.uint8).reshape(bug.size[1], bug.size[0], 3)

plt.gray()
plt.imshow(arr)
plt.colorbar()
plt.show()

plt.figure()
plt.gray()
plt.subplot(121)
plt.imshow(bug)

zbug = bug[100:350, 140:350]

plt.subplot(122)
plt.imshow(zbug)
plt.show()