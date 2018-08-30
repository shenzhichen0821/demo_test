import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(plt.figure())

x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'), edgecolor='k')
ax.contourf(x, y, z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)

plt.show()
