import matplotlib.pyplot as plt
import fractions as frac
from math import log
import numpy as np
import math
from matplotlib.animation import FuncAnimation
import sympy as sp


points = [[p/float(q), 1/float(q), log(float(q))] \
    for q in range(1, 50) \
    for p in range(0, q+1)\
    if math.gcd(p,q) == 1]
plt.axis('off')
x,y,color=zip(*points)
plt.scatter(x,y, c=color, s=3, edgecolor='none', cmap='winter')

plt.show()
