#
#
# import matplotlib.pyplot as plt  # 绘图用的模块
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D  # 绘制3D坐标的函数
#
#
# def fun(x1, x2):
#     # return np.power((x-10), 3) + np.power((y-20), 3)
#     return 100 * np.math.sqrt(abs(x2 - 0.01 * x1 * x1)) + 0.01 * abs(x1 + 10)
#
#
# fig1 = plt.figure()  # 创建一个绘图对象
# ax = Axes3D(fig1)  # 用这个绘图对象创建一个Axes对象(有3D坐标)
# X = np.arange(-15, -5, 0.1)
# Y = np.arange(-3, 3, 0.1)  # 创建了从-2到2，步长为0.1的arange对象
# # 至此X,Y分别表示了取样点的横纵坐标的可能取值
# # 用这两个arange对象中的可能取值一一映射去扩充为所有可能的取样点
# X, Y = np.meshgrid(X, Y)
# Z = fun(X, Y)  # 用取样点横纵坐标去求取样点Z坐标
# plt.title("function")  # 总标题
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm)  # 用取样点(x,y,z)去构建曲面
# ax.set_xlabel('x label', color='r')
# ax.set_ylabel('y label', color='g')
# ax.set_zlabel('z label', color='b')  # 给三个坐标轴注明
# plt.show()  # 显示模块中的所有绘图对象


import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def bukin_function(x1, x2):
    return 100 * np.sqrt(abs(x2 - 0.01 * x1 * x1)) + 0.01 * abs(x1 + 10)


def cross_in_tray_function(x1, x2):
    # return (-0.0001 * (abs(np.sin(x1) * np.sin(x2) * np.exp(abs(100 - ((np.sqrt(x1 * x1 + x2 * x2)) / np.pi)))) + 1)) ** 0.1
    x = abs(100 - (np.sqrt(x1 ** 2 + x2 ** 2) / np.pi))
    return -0.0001 * ((np.sin(x1) * np.sin(x2)) ** x + 1) ** 0.1


fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-10, -10, 0.1)
Y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(X, Y)
Z = cross_in_tray_function(X, Y)

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
ax.set_title("cross in tray function")

plt.show()
