import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import function as fn


def Dawn():
    fig = plt.figure()
    ax = Axes3D(fig)
    X1 = np.arange(-512, 512, 5)
    X2 = np.arange(-512, 512, 5)
    X, Y = np.meshgrid(X1, X2)
    array = [X, Y]
    F = fn.eggholder(array)
    ax.plot_surface(X, Y, F, rstride=1, cstride=1, cmap=plt.cm.rainbow)
    #plt.savefig('../images/functions/eggholder.png', dpi=200)
    plt.show()


Dawn()
