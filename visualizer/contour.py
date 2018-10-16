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
# N = np.arange(0, 1, 0.01)  # 用来指明等高线对应的值为多少时才出现对应图线
fig = plt.figure(figsize=(20, 10))
fig.add_subplot()
CS = plt.contour(X, Y, Z, 20, cmap=mpl.    cm.jet)  # 画出等高线图，cmap表示颜色的图层。
plt.plot(pd[0], pd[1], 'ro')
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)  # 在等高线图里面加入每条线对应的值
plt.colorbar(CS)  # 标注右侧的图例
plt.title(filename)
plt.savefig('../images/statistics/after50.png', dpi=200)
plt.show()
