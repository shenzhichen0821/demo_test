import math
import numpy as np
import matplotlib.pyplot as plt

plot_set = np.arange(1, 100, 1)
plt.plot(plot_set, [100 / x + 2 * math.sqrt(x) for x in plot_set])
plt.show()