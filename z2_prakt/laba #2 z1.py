import matplotlib.pyplot as plt
import numpy as np
from math import sin

def y(x):
    return sin(10*x)/(x+0.1)

x = np.arange(0, 3, 0.01)

y_ready = []
for i in range(len(x)):
    y_ready.append(y(x[i]))

plt.plot(x, y_ready)
plt.show()