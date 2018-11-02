from Algorithms.algorithm import Algorithm
import pandas as pd
import numpy as np
import random
import math
import os


class CuckooSearch(Algorithm):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.discovery_rate = kwargs.pop('discovery_rate', 0.25)
        self.alpha_val = kwargs.pop('alpha_val', 0.01)
        self.lambda_val = kwargs.pop('lambda_val', 1.5)

    def initial_position(self):
        position = pd.DataFrame(np.zeros((self.population, self.func.dimension)))
        position['Fitness'] = 0.0
        for i in range(0, self.population):
            for j in range(0, self.func.dimension):
                position.iloc[i, j] = random.uniform(self.func.min_values[j], self.func.max_values[j])
            position.iloc[i, -1] = self.target_function(position.iloc[i, 0:position.shape[1] - 1])
        return position

    def levy_flight(self):
        x1 = math.sin((self.lambda_val - 1.0) * (random.uniform(-0.5 * math.pi, 0.5 * math.pi))) / (
            math.pow(math.cos((random.uniform(-0.5 * math.pi, 0.5 * math.pi))), (1.0 / (self.lambda_val - 1.0))))
        x2 = math.pow((math.cos((2.0 - self.lambda_val) * (random.uniform(-0.5 * math.pi, 0.5 * math.pi))) / (
            -math.log(random.uniform(0.0, 1.0)))), ((2.0 - self.lambda_val) / (self.lambda_val - 1.0)))
        return x1 * x2

    '''choose a bird randomly, return the better one'''

    def replace_bird(self, position):
        random_bird = np.random.randint(position.shape[0], size=1)[0]
        new_solution = pd.DataFrame(np.zeros((1, position.shape[1])))

        for j in range(0, position.shape[1] - 1):
            new_solution.iloc[0, j] = position.iloc[random_bird, j] + self.alpha_val * self.levy_flight() * \
                                      position.iloc[random_bird, j] * (
                                              int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1))
            if new_solution.iloc[0, j] > self.func.max_values[j]:
                new_solution.iloc[0, j] = self.func.max_values[j]
            elif new_solution.iloc[0, j] < self.func.min_values[j]:
                new_solution.iloc[0, j] = self.func.min_values[j]
        new_solution.iloc[0, -1] = self.target_function(new_solution.iloc[0, 0:new_solution.shape[1] - 1])

        if position.iloc[random_bird, -1] > new_solution.iloc[0, -1]:
            for j in range(0, position.shape[1]):
                position.iloc[random_bird, j] = new_solution.iloc[0, j]
        return position

    def update_positions(self, position):
        updated_position = position.copy(deep=True)
        abandoned_nests = math.ceil(self.discovery_rate * updated_position.shape[0]) + 1
        random_bird_j = np.random.randint(position.shape[0], size=1)[0]
        random_bird_k = np.random.randint(position.shape[0], size=1)[0]
        while random_bird_j == random_bird_k:
            random_bird_j = np.random.randint(position.shape[0], size=1)[0]
        nest_list = list(position.nlargest(abandoned_nests - 1, "Fitness").index.values)

        for i in range(0, updated_position.shape[0]):
            for j in range(0, len(nest_list)):
                rand = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
                if i == nest_list[j] and rand > self.discovery_rate:
                    for k in range(0, updated_position.shape[1] - 1):
                        rand = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
                        updated_position.iloc[i, k] = updated_position.iloc[i, k] + rand * (
                                updated_position.iloc[random_bird_j, k] - updated_position.iloc[random_bird_k, k])
                        if updated_position.iloc[i, k] > self.func.max_values[k]:
                            updated_position.iloc[i, k] = self.func.max_values[k]
                        elif updated_position.iloc[i, k] < self.func.min_values[k]:
                            updated_position.iloc[i, k] = self.func.min_values[k]
            updated_position.iloc[i, -1] = self.target_function(
                updated_position.iloc[i, 0:updated_position.shape[1] - 1])

        return updated_position

    def run(self):
        count = 0
        position = self.initial_position()
        best_ind = position.iloc[position['Fitness'].idxmin(), :].copy(deep=True)
        while not self.stop_condition(count, best_ind[-1]):
            print("Iteration = ", count, " of ", self.iterations, " f(x) = ", best_ind[-1])

            for i in range(0, position.shape[0]):
                position = self.replace_bird(position)
            position = self.update_positions(position)

            if best_ind[-1] > position.iloc[position['Fitness'].idxmin(), :][-1]:
                best_ind = position.iloc[position['Fitness'].idxmin(), :].copy(deep=True)

            self.current_sulotion.append(best_ind[-1])

            count = count + 1

        self.best_solution = best_ind

        return best_ind


if __name__ == '__main__':
    from benchmark.Benchmark import Ackley

    ac = Ackley()
    cs = CuckooSearch()
    cs.run()
    cs.save()
