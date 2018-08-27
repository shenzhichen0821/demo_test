import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(plt.figure())
x = np.arange(1, 100, 1)
y = np.arange(1, 100, 1)
x, y = np.meshgrid(x, y)
z = np.array(100/x + x/y + y)

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
plt.xlabel('x axis')
plt.ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()