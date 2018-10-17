# -*- coding: utf-8 -*-

'''
======================================
|           kiterun                  |
|		   2017/08/11                |
|		 kiterun@126.com             |
======================================
'''

import math
import sys
from time import time

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import function as fn
from simulated_annealing.simAnneal_FUNC import OptSolution
from simulated_annealing.simAnneal_FUNC import SimAnneal


def func(w):
    x, = w
    fx = x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
    return fx


def func2(w):
    # x, y = w
    # fxy = y * np.sin(2 * np.pi * x) + x * np.cos(2 * np.pi * y)
    # return fxy
    return fn.michalewicz(w)



def run_draw():

    targ = SimAnneal(target_text='min')
    init = sys.maxsize
    xyRange = [[0, np.pi], [0, np.pi]]
    t_start = time()

    calculate = OptSolution(Markov_chain=1000, result=init, val_nd=[0, 0])
    output = calculate.soulution(SA_newV=targ.newVar, SA_preV=targ.preVar, SA_juge=targ.juge,
                                 juge_text='min', ValueRange=xyRange, func=func2)
    t_end = time()
    # print(city_pos)
    print('Running %.4f seconds' % (t_end - t_start))

    # plot animation
    fig = plt.figure()
    ax = Axes3D(fig)
    xv = np.linspace(xyRange[0][0], xyRange[0][1], 200)
    yv = np.linspace(xyRange[1][0], xyRange[1][1], 200)
    xv, yv = np.meshgrid(xv, yv)
    zv = func2([xv, yv])
    ax.plot_surface(xv, yv, zv, rstride=1, cstride=1, cmap='GnBu', alpha=1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    x, y, z = output[0][0], output[0][1], output[1]
    ax.scatter(x, y, z, c='r', marker='o')

    plt.savefig('SA_min0.png')
    plt.show()


if __name__ == '__main__':
    run_draw()
