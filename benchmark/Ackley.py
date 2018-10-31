import numpy as np


class Ackley:
    def __init__(self, min_values=[-32.768] * 2, max_values=[32.768] * 2, dimension=2):
        self.min_values = min_values
        self.max_values = max_values
        self.dimension = dimension

    def get_optimum(self):
        return [0] * self.dimension, 0

    @staticmethod
    def eval(array, a=20, b=0.2, c=2 * np.pi):
        '''
        at d=2 : xi ∈ [-32.768, 32.768] , f([0,0]) = 4.440892098500626e-16
        at d=5 : xi ∈ [-32.768, 32.768] , f([0,0,0,0,0]) = 4.440892098500626e-16
        '''

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
