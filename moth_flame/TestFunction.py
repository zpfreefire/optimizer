import numpy as np
import function as fn

class TestFunction:
    """
    测试函数
    """

    def __init__(self, func_name):
        if func_name == 'F1':
            self.func = self.F1
            self.dim = 10
            self.lb = np.zeros(self.dim)
            self.ub = np.zeros(self.dim)

            for i in range(self.dim):
                self.lb[i] = -100
                self.ub[i] = 100

    def generate_feasible_solutions(self, n=1):
        """
        生成可行解
        :return: 可行解
        """

        x = np.zeros((n, self.dim))
        for i in range(self.dim):
            x[:, i] = self.lb[i] + np.random.rand(n) * (self.ub[i] - self.lb[i])

        return x

    def calculate_fitness_value(self, x):
        """
        计算目标函数值
        :param x: 自变量
        :return: 函数值
        """

        y = self.func(x)

        return y

    @staticmethod
    def F1(x):
        y = np.zeros(x.shape[0])
        for i in range(x.shape[0]):
            y[i] = (x[i] ** 2).sum()
        return y
        #return fn.crossit(x)


def test():
    """
    test function
    :return:
    """

    problem = TestFunction('F1')
    x = problem.generate_feasible_solutions(2)
    print(x)

    y = problem.F1(x)
    print(y)


if __name__ == '__main__':
    test()