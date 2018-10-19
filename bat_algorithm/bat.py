import math

import numpy as np
import os
import pandas as pd
import random

import function as fn


def initial_position(swarm_size=3, min_values=[-5, -5], max_values=[5, 5]):
    position = pd.DataFrame(np.zeros((swarm_size, len(min_values))))
    for i in range(0, len(min_values)):
        position['Velocity_' + str(i)] = 0.0
    position['Fitness'] = 0.0
    position['Frequency'] = 0.0
    position['Rate'] = 0.0
    position['Loudness'] = 0.0
    for i in range(0, swarm_size):
        for j in range(0, len(min_values)):
            position.iloc[i, j] = random.uniform(min_values[j], max_values[j])
    for i in range(0, swarm_size):
        position.iloc[i, -4] = target_function(position.iloc[i, 0:len(min_values)])
        position.iloc[i, -2] = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
        position.iloc[i, -1] = random.uniform(1, 2)
    return position


def update_position(position, best_ind, alpha=0.9, gama=0.9, fmin=0, fmax=10, dimensions=2, count=0,
                    min_values=[-5, -5], max_values=[5, 5]):
    position_temp = pd.DataFrame(np.zeros((position.shape[0], position.shape[1])))
    rate = pd.DataFrame(np.zeros((position.shape[0], 1)))
    for i in range(0, position.shape[0]):
        beta = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
        position.iloc[i, -3] = fmin + (fmax - fmin) * beta
        rate.iloc[i, 0] = position.iloc[i, -2]
        for j in range(dimensions, 2 * dimensions):
            position.iloc[i, j] = position.iloc[i, j] + (position.iloc[i, j - dimensions] - best_ind[j]) * \
                                  position.iloc[i, -3]
        for k in range(0, dimensions):
            position_temp.iloc[i, k] = position.iloc[i, k] + position.iloc[i, k + dimensions]
            if (position_temp.iloc[i, k] > max_values[k]):
                position_temp.iloc[i, k] = max_values[k]
                position.iloc[i, k + dimensions] = 0
            elif (position_temp.iloc[i, k] < min_values[k]):
                position_temp.iloc[i, k] = min_values[k]
                position.iloc[i, k + dimensions] = 0
        position_temp.iloc[i, -4] = target_function(position_temp.iloc[i, 0:dimensions])
        rand = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
        if (rand > position.iloc[i, -2]):
            for L in range(0, dimensions):
                position_temp.iloc[i, L] = best_ind[L] + random.uniform(-1, 1) * position['Loudness'].mean()
                if (position_temp.iloc[i, L] > max_values[L]):
                    position_temp.iloc[i, L] = max_values[L]
                    position.iloc[i, L + dimensions] = 0
                elif (position_temp.iloc[i, L] < min_values[L]):
                    position_temp.iloc[i, L] = min_values[L]
                    position.iloc[i, L + dimensions] = 0
            position_temp.iloc[i, -4] = target_function(position_temp.iloc[i, 0:dimensions])
        rand = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
        if (rand < position.iloc[i, -1] and position_temp.iloc[i, -4] <= position.iloc[i, -4]):
            for m in range(0, dimensions):
                position.iloc[i, m] = position_temp.iloc[i, m]
            position.iloc[i, -4] = target_function(position.iloc[i, 0:dimensions])
            position.iloc[i, -2] = rate.iloc[i, 0] * (1 - math.exp(-gama * count))
            position.iloc[i, -1] = alpha * position.iloc[i, -1]
        if (best_ind[-4] > position.iloc[position['Fitness'].idxmin(), :][-4]):
            for n in range(0, len(best_ind)):
                best_ind[n] = position.iloc[i, n]
    return position, best_ind


def bat_algorithm(swarm_size=3, min_values=[-5, -5], max_values=[5, 5], iterations=50, alpha=0.9, gama=0.9, fmin=0,
                  fmax=10):
    count = 1
    position = initial_position(swarm_size=swarm_size, min_values=min_values, max_values=max_values)
    best_ind = position.iloc[position['Fitness'].idxmin(), :].copy(deep=True)
    position, best_ind = update_position(position, best_ind, alpha=alpha, gama=gama, fmin=fmin, fmax=fmax,
                                         dimensions=len(min_values), count=count, min_values=min_values,
                                         max_values=max_values)
    while (count <= iterations):
        print("Iteration = ", count, " of ", iterations, " f(x) = ", best_ind['Fitness'])

        position, best_ind = update_position(position, best_ind, alpha=alpha, gama=gama, fmin=fmin, fmax=fmax,
                                             dimensions=len(min_values), count=count, min_values=min_values,
                                             max_values=max_values)
        count = count + 1

    print(best_ind[0:len(min_values)])
    print("f(x) = ", best_ind['Fitness'])
    return best_ind


def target_function(variables_values=[0, 0]):
    return fn.michalewicz(variables_values)


ba = bat_algorithm(swarm_size=25, min_values=[0, 0], max_values=[np.pi, np.pi],
                   iterations=200, alpha=1.0, gama=0.8, fmin=0, fmax=2)
