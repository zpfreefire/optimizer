import math

import numpy  as np
import os
import pandas as pd
import random
from benchmark import function as fn


# Function: Initialize Variables
def initial_moths(swarm_size=3, min_values=[-5, -5], max_values=[5, 5]):
    position = pd.DataFrame(np.zeros((swarm_size, len(min_values))))
    position['Fitness'] = 0.0
    for i in range(0, swarm_size):
        for j in range(0, len(min_values)):
            position.iloc[i, j] = random.uniform(min_values[j], max_values[j])
        position.iloc[i, -1] = target_function(position.iloc[i, 0:position.shape[1] - 1])
    return position


# Function: Update Flames
def update_flames(flames, position):
    population = pd.concat([flames, position])
    flames = population.nsmallest(flames.shape[0], "Fitness").copy(deep=True)
    return flames


# Function: Update Position
def update_position(position, flames, flame_number=1, b_constant=1, a_linear_component=1, min_values=[-5, -5],
                    max_values=[5, 5]):
    for i in range(0, position.shape[0]):
        for j in range(0, len(min_values)):
            if (i <= flame_number):
                flame_distance = abs(flames.iloc[i, j] - position.iloc[i, j])
                b_constant = b_constant
                rnd_1 = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
                rnd_2 = (a_linear_component - 1) * rnd_1 + 1
                position.iloc[i, j] = flame_distance * math.exp(b_constant * rnd_2) * math.cos(rnd_2 * 2 * math.pi) + \
                                      flames.iloc[i, j]
            elif (i > flame_number):
                flame_distance = abs(flames.iloc[i, j] - position.iloc[i, j])
                b_constant = b_constant
                rnd_1 = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
                rnd_2 = (a_linear_component - 1) * rnd_1 + 1
                position.iloc[i, j] = flame_distance * math.exp(b_constant * rnd_2) * math.cos(rnd_2 * 2 * math.pi) + \
                                      flames.iloc[flame_number, j]
            if (position.iloc[i, j] > max_values[j]):
                position.iloc[i, j] = max_values[j]
            elif (position.iloc[i, j] < min_values[j]):
                position.iloc[i, j] = min_values[j]
        position.iloc[i, -1] = target_function(position.iloc[i, 0:position.shape[1] - 1])
    return position



def moth_flame_algorithm(swarm_size=3, min_values=[-5, -5], max_values=[5, 5], generations=50, b_constant=1):
    position = initial_moths(swarm_size=swarm_size, min_values=min_values, max_values=max_values)
    flames = position.nsmallest(position.shape[0], "Fitness").copy(deep=True)
    count = 0
    best_moth = flames.iloc[0, :].copy(deep=True)

    while (count <= generations):
        print("Generation: ", count, " of ", generations, " f(x) = ", best_moth[-1])

        flame_number = round(position.shape[0] - count * ((position.shape[0] - 1) / generations))
        a_linear_component = -1 + count * ((-1) / generations)
        position = update_position(position, flames, flame_number=flame_number, b_constant=b_constant,
                                   a_linear_component=a_linear_component, min_values=min_values, max_values=max_values)
        flames = update_flames(flames, position)
        count = count + 1
        if (flames.iloc[0, :][-1] < best_moth[-1]):
            best_moth = flames.iloc[0, :].copy(deep=True)

    print(best_moth)
    return best_moth


def target_function(variables_values=[0, 0]):
    return fn.michalewicz(variables_values)


mfa = moth_flame_algorithm(swarm_size=20, min_values=[0, 0], max_values=[np.pi, np.pi],
                           generations=100, b_constant=1)
