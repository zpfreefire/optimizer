import csv
import math

import numpy as np
import os
import pandas as pd
import random

import function as func
import datetime


# Function: Initialize Variables
def initial_position(birds=3, min_values=[5, 5], max_values=[5, 5]):
    position = pd.DataFrame(np.zeros((birds, len(min_values))))
    position['Fitness'] = 0.0
    for i in range(0, birds):
        for j in range(0, len(min_values)):
            position.iloc[i, j] = random.uniform(min_values[j], max_values[j])
        position.iloc[i, -1] = target_function(position.iloc[i, 0:position.shape[1] - 1])
    return position


# Function: Levy Distribution
def levy_flight(mean):
    x1 = math.sin((mean - 1.0) * (random.uniform(-0.5 * math.pi, 0.5 * math.pi))) / (
        math.pow(math.cos((random.uniform(-0.5 * math.pi, 0.5 * math.pi))), (1.0 / (mean - 1.0))))
    x2 = math.pow((math.cos((2.0 - mean) * (random.uniform(-0.5 * math.pi, 0.5 * math.pi))) / (
        -math.log(random.uniform(0.0, 1.0)))), ((2.0 - mean) / (mean - 1.0)))
    return x1 * x2


# Function: Replace Bird
def replace_bird(position, alpha_value=0.01, lambda_value=1.5, min_values=[-5, -5], max_values=[5, 5]):
    random_bird = np.random.randint(position.shape[0], size=1)[0]
    new_solution = pd.DataFrame(np.zeros((1, position.shape[1])))

    for j in range(0, position.shape[1] - 1):
        new_solution.iloc[0, j] = position.iloc[random_bird, j] + alpha_value * levy_flight(lambda_value) * \
                                  position.iloc[random_bird, j] * (
                                          int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1))
        if new_solution.iloc[0, j] > max_values[j]:
            new_solution.iloc[0, j] = max_values[j]
        elif new_solution.iloc[0, j] < min_values[j]:
            new_solution.iloc[0, j] = min_values[j]
    new_solution.iloc[0, -1] = target_function(new_solution.iloc[0, 0:new_solution.shape[1] - 1])

    if position.iloc[random_bird, -1] > new_solution.iloc[0, -1]:
        for j in range(0, position.shape[1]):
            position.iloc[random_bird, j] = new_solution.iloc[0, j]
    return position



# arr = position[[0, 1]].values
    # filename = ("../statistics/cs/final_position/%s.csv" % tim)
    # f = open(filename, "w", newline="")
    # writer = csv.writer(f)
    # for row in arr:
    #     writer.writerow(row)
    # f.close()
# Function: Update Positions
def update_positions(position, discovery_rate=0.25, min_values=[-5, -5], max_values=[5, 5]):
    updated_position = position.copy(deep=True)
    abandoned_nests = math.ceil(discovery_rate * updated_position.shape[0]) + 1
    random_bird_j = np.random.randint(position.shape[0], size=1)[0]
    random_bird_k = np.random.randint(position.shape[0], size=1)[0]
    while random_bird_j == random_bird_k:
        random_bird_j = np.random.randint(position.shape[0], size=1)[0]
    nest_list = list(position.nlargest(abandoned_nests - 1, "Fitness").index.values)

    for i in range(0, updated_position.shape[0]):
        for j in range(0, len(nest_list)):
            rand = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
            if i == nest_list[j] and rand > discovery_rate:
                for k in range(0, updated_position.shape[1] - 1):
                    rand = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
                    updated_position.iloc[i, k] = updated_position.iloc[i, k] + rand * (
                            updated_position.iloc[random_bird_j, k] - updated_position.iloc[random_bird_k, k])
                    if updated_position.iloc[i, k] > max_values[k]:
                        updated_position.iloc[i, k] = max_values[k]
                    elif updated_position.iloc[i, k] < min_values[k]:
                        updated_position.iloc[i, k] = min_values[k]
        updated_position.iloc[i, -1] = target_function(updated_position.iloc[i, 0:updated_position.shape[1] - 1])

    return updated_position


# CS Function
def cuckoo_search(birds=3, discovery_rate=0.25, alpha_value=0.01, lambda_value=1.5, min_values=[-5, -5],
                  max_values=[5, 5], iterations=50, optimum=0.0):
    count = 0
    position = initial_position(birds=birds, min_values=min_values, max_values=max_values)
    best_ind = position.iloc[position['Fitness'].idxmin(), :].copy(deep=True)
    while count <= iterations:
        print("Iteration = ", count, " of ", iterations, " f(x) = ", best_ind[-1])

        for i in range(0, position.shape[0]):
            position = replace_bird(position, alpha_value=alpha_value, lambda_value=lambda_value, min_values=min_values,
                                    max_values=max_values)
        position = update_positions(position, discovery_rate=discovery_rate, min_values=min_values,
                                    max_values=max_values)

        if best_ind[-1] > position.iloc[position['Fitness'].idxmin(), :][-1]:
            best_ind = position.iloc[position['Fitness'].idxmin(), :].copy(deep=True)

        count = count + 1

    print(best_ind)
    # return best_ind


# Function to be Minimized. Solution ->  f(-10, 1) = 0
def target_function(variables_values=[0, 0]):
    return func.target_function(variables_values)


def main():
    cuckoo_search(birds=10, discovery_rate=0.25, alpha_value=0.01, lambda_value=1.5,
                  min_values=[np.pi] * 5,
                  max_values=[np.pi] * 5, iterations=200)


main()
