import numpy as np
from benchmark.Benchmark import Benchmarks


class Ackley(Benchmarks):
    def __init__(self, min_values=[-32.768] * 2, max_values=[32.768] * 2, dimension=2):
        super(Ackley, self).__init__(min_values, max_values, dimension)

    def get_optimum(self):
        return [0] * self.dimension, 0

    @staticmethod
    def eval(array, a=20, b=0.2, c=2 * np.pi):
        d = len(array)

        sum1 = 0
        sum2 = 0
        for i in range(d):
            xi = array[i]
            sum1 = sum1 + xi ** 2
            sum2 = sum2 + np.cos(c * xi)
        term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
        term2 = -np.exp(sum2 / d)

        fitness = term1 + term2 + a + np.exp(1)

        return fitness
