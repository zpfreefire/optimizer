import math

import numpy  as np
import os
import pandas as pd
import random


# Function: Initialize Variables
def initial_fireflies(swarm_size=3, min_values=[-5, -5], max_values=[5, 5]):
    position = pd.DataFrame(np.zeros((swarm_size, len(min_values))))
    position['Ligth_0'] = 0.0
    for i in range(0, swarm_size):
        for j in range(0, len(min_values)):
            position.iloc[i, j] = random.uniform(min_values[j], max_values[j])
        position.iloc[i, -1] = target_function(position.iloc[i, 0:position.shape[1] - 1])
    return position


# Function: Distance Calculations
def euclidean_distance(x, y):
    distance = 0
    for j in range(0, len(x)):
        distance = (x.iloc[j] - y.iloc[j]) ** 2 + distance
    return distance ** (1 / 2)


# Function: Beta Value
def beta_value(x, y, gama=1, beta_0=1):
    rij = euclidean_distance(x, y)
    beta = beta_0 * math.exp(-gama * (rij) ** 2)
    return beta


# Function: Ligth Intensity
def ligth_value(light_0, x, y, gama=1):
    rij = euclidean_distance(x, y)
    light = light_0 * math.exp(-gama * (rij) ** 2)
    return light


# Function: Update Position
def update_position(position, x, y, alpha_0=0.2, beta_0=1, gama=1, firefly=0, min_values=[-5, -5], max_values=[5, 5]):
    for j in range(0, len(x)):
        epson = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1) - (1 / 2)
        position.iloc[firefly, j] = x.iloc[j] + beta_value(x, y, gama=gama, beta_0=beta_0) * (
                y.iloc[j] - x.iloc[j]) + alpha_0 * epson
        if (position.iloc[firefly, j] > max_values[j]):
            position.iloc[firefly, j] = max_values[j]
        elif (position.iloc[firefly, j] < min_values[j]):
            position.iloc[firefly, j] = min_values[j]
    position.iloc[firefly, -1] = target_function(position.iloc[firefly, 0:position.shape[1] - 1])
    return position


# FA Function
def firefly_algorithm(swarm_size=3, min_values=[-5, -5], max_values=[5, 5], generations=50, alpha_0=0.2, beta_0=1,
                      gama=1):
    position = initial_fireflies(swarm_size=swarm_size, min_values=min_values, max_values=max_values)
    count = 0
    while (count <= generations):
        print("Generation: ", count, " of ", generations, " f(x) = ",
              position.iloc[position['Ligth_0'].idxmin(), :][-1])
        for i in range(0, swarm_size):
            for j in range(0, swarm_size):
                if (i != j):
                    firefly_i = position.iloc[i, 0:position.shape[1] - 1].copy(deep=True)
                    firefly_j = position.iloc[j, 0:position.shape[1] - 1].copy(deep=True)
                    ligth_i = ligth_value(position.iloc[i, -1], firefly_i, firefly_j, gama=gama)
                    ligth_j = ligth_value(position.iloc[j, -1], firefly_i, firefly_j, gama=gama)
                    if (ligth_i > ligth_j):
                        position = update_position(position, firefly_i, firefly_j, alpha_0=alpha_0, beta_0=beta_0,
                                                   gama=gama, firefly=i, min_values=min_values, max_values=max_values)
        count = count + 1
    best_firefly = position.iloc[position['Ligth_0'].idxmin(), :].copy(deep=True)
    return best_firefly


def target_function(variables_values=[0, 0]):
    func_value = 4 * variables_values[0] ** 2 - 2.1 * variables_values[0] ** 4 + (1 / 3) * variables_values[0] ** 6 + \
                 variables_values[0] * variables_values[1] - 4 * variables_values[1] ** 2 + 4 * variables_values[1] ** 4
    return func_value


firefly_algorithm(swarm_size=25, min_values=[-5, -5], max_values=[5, 5], generations=50, alpha_0=0.2, beta_0=1, gama=1)