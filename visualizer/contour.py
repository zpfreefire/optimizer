import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import function as fn

filename = "../statistics/cs/after50/2018-10-16_11:44:25.csv"

pd = pd.read_csv(filename, header=None)


def process_signals(x, y):
    array = [x, y]
    return fn.michalewicz(array)


x = np.arange(0, 4.5, 0.01)
y = np.arange(0, 4.5, 0.01)
X, Y = np.meshgrid(x, y)
Z = process_signals(X, Y)

fig = plt.figure(figsize=(20, 10))
fig.add_subplot()
CS = plt.contour(X, Y, Z, 16, cmap=mpl.cm.jet)
plt.plot(pd[0], pd[1], 'ro')
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)
# plt.title(filename)
plt.savefig('../images/statistics/michalewicz/after50.png', dpi=200)
plt.show()
