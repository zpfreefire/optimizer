import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_pic(X, Y, Z, title):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.rainbow)
    # ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
    ax.set_title(title)
    #plt.savefig("%s.png" % title,bbox_inches='tight')
    plt.show()


def get_X_AND_Y(X_min, X_max, Y_min, Y_max):
    X = np.arange(X_min, X_max, 1)
    Y = np.arange(Y_min, Y_max, 1)
    X, Y = np.meshgrid(X, Y)
    return X, Y

#  Bohachevsky 1 Function 测试函数
def Bohachevsky(X_min = -100, X_max = 100, Y_min = -100, Y_max = 100):
    X, Y = get_X_AND_Y(X_min, X_max, Y_min, Y_max)
    Z = X**2 + 2*(Y**2) - 0.3*(np.cos(3*np.pi*X)) - 0.4*(np.cos(4*np.pi*Y)) +0.7
    return X, Y, Z, "Bohachevsky Function "


X, Y, Z, title = Bohachevsky()
draw_pic(X, Y, Z, title)