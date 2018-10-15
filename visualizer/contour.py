import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def process_signals(x, y):
    return (1 - (x ** 2 + y ** 2)) * np.exp(-y ** 3 / 3)


x = np.arange(-1.5, 1.5, 0.1)
y = np.arange(-1.5, 1.5, 0.1)
X, Y = np.meshgrid(x, y)
Z = process_signals(X, Y)
N = np.arange(-1, 1.5, 0.3)  # 用来指明等高线对应的值为多少时才出现对应图线
fig = plt.figure()  # 设定图形大小
fig.add_subplot()  # 画第一张图
CS = plt.contour(Z, N, linewidth=2, cmap=mpl.cm.jet)  # 画出等高线图，cmap表示颜色的图层。
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)  # 在等高线图里面加入每条线对应的值
# plt.colorbar(CS)  # 标注右侧的图例
# fig.add_subplot(122)  # 画第二张图
# CS = plt.contourf(Z, N, linewidth=2, cmap=mpl.cm.jet)  # 画出等高线填充图，cmap表示颜色的图层。
# plt.colorbar(CS)  # 标注右侧的图例
plt.show()
