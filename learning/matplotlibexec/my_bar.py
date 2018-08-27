import matplotlib.pyplot as plt
import numpy as np

n = 12
x = np.arange(n)
y1 = np.random.uniform(0, 1, size=n,)
y2 = -np.random.uniform(0, 1, size=n,)

plt.bar(x, y1, facecolor='#9999ff', edgecolor='w')
plt.bar(x, y2, facecolor='#ff9999', edgecolor='w')

for i,j in zip(x, y1):
    plt.text(i + 0.4, j + 0.05, "%.2f" % j, ha='center', va='bottom')

for i,j in zip(x, y2):
    plt.text(i + 0.4, j - 0.05, "%.2f" % j, ha='center', va='bottom')

plt.xlim(-1, n)
plt.ylim(-1.25, 1.25)
plt.xticks(())
plt.yticks(())
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')

plt.show()
