import matplotlib.pyplot as plt
import numpy as np
import math

# figure
x = np.arange(-50,50,0.1)
y1 = 2 * x + 1
y2 = [math.sin(i) for i in x]

plt.figure()
plt.plot(x, y1)

plt.figure()
plt.plot(x, y2, color='red', linestyle='--')

plt.xlim((-10,10))
plt.ylim((-1.5,1.5))

plt.xlabel('I am x')
plt.ylabel('I am y')

plt.xticks(np.linspace(-10, 10, 21))
plt.yticks([-1.5, 0, 1.5],
           ['low', 'zero', 'high'])

#axis
plt.figure()
y3 = x ** 3
y_1, = plt.plot(x, y1, label='y_1')
y_2, = plt.plot(x, y2, label='y_2')
y_3, = plt.plot(x, y3, label='y_3')
plt.xlim((-2, 2))
plt.ylim((-8, 8))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.legend(handles=[y_1, y_2, y_3], labels=["replace1", "replace2", "replace3"], loc='best')
plt.show()

