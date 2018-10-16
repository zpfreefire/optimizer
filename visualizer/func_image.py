import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import function as fn


def Dawn():
    fig = plt.figure()
    ax = Axes3D(fig)
    X1 = np.arange(0, 4, 0.02)
    X2 = np.arange(0, 4, 0.02)
    X, Y = np.meshgrid(X1, X2)
    array = [X, Y]
    F = fn.michalewicz(array)
    ax.plot_surface(X, Y, F, rstride=1, cstride=1, cmap=plt.cm.rainbow)
    #plt.savefig('../images/michalewicz.png', dpi=100)
    plt.show()


Dawn()
