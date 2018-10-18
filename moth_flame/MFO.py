import numpy as np
from moth_flame.TestFunction import TestFunction


class MFO:

    """飞蛾扑火优化算法"""

    def __init__(self, size, max_iter, problem):
        """
        :param size: 飞蛾数量
        :param max_iter: 最大迭代次数
        :param problem: 问题
        """
        self.size = size
        self.max_iter = max_iter
        self.problem = problem
        self.convergence_curve = np.zeros(max_iter)

        # 初始化飞蛾种群
        self.moth_pos = problem.generate_feasible_solutions(size)

        # 计算种群适应度值
        self.moth_fitness = problem.calculate_fitness_value(self.moth_pos)

        # 初始化火焰适应度值
        self.flame_fitness = self.moth_fitness.copy()

        # 火焰排序
        index = self.flame_fitness.argsort()
        self.flame_fitness.sort()

        # 初始化火焰
        self.flame_pos = self.moth_pos.copy()
        for i in range(self.flame_pos.shape[0]):
            self.flame_pos[i] = self.moth_pos[index[i]]

    def solve(self):
        """
        求解
        """

        iteration = 0

        while iteration < self.max_iter:

            previous_population = self.moth_pos.copy()
            previous_fitness = self.moth_fitness.copy()

            flame_no = round(self.size - iteration * ((self.size - 1) / self.max_iter))
            a = -1 - iteration / self.max_iter

            for i in range(self.moth_pos.shape[0]):
                for j in range(self.moth_pos.shape[1]):
                    distance_to_flame = abs(self.flame_pos[i][j] - self.moth_pos[i][j])
                    b = 1
                    t = (a - 1) * np.random.rand() + 1
                    if i < flame_no:
                        self.moth_pos[i][j] = distance_to_flame * np.exp(b * t) * np.cos(t * 2 * np.pi) + \
                                              self.flame_pos[i][j]
                    else:
                        self.moth_pos[i][j] = distance_to_flame * np.exp(b * t) * np.cos(t * 2 * np.pi) + \
                                              self.flame_pos[flame_no][j]

            self.moth_fitness = self.problem.calculate_fitness_value(self.moth_pos)

            double_population = np.append(previous_population, self.moth_pos, axis=0)
            double_fitness = np.append(previous_fitness, self.moth_fitness)

            index = double_fitness.argsort()
            double_fitness.sort()

            self.flame_fitness = double_fitness[0:self.size].copy()
            for i in range(self.flame_pos.shape[0]):
                self.flame_pos[i] = double_population[index[i]]

            self.convergence_curve[iteration] = double_fitness[0]

            if np.mod(iteration + 1, 50) == 0:
                print('At iteration %d the best fitness is %f' % (iteration + 1, self.convergence_curve[iteration]))

            iteration += 1


def test():
    """
    test function
    :return:
    """

    problem = TestFunction('F1')
    mfo = MFO(30, 1000, problem)

    mfo.solve()


if __name__ == '__main__':
    test()