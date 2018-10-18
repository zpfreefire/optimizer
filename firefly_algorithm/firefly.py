import random
import numpy as np
import datetime

import function as fn

def distance(firefly_a, firefly_b):
    sum = 0
    for i in range(len(firefly_a.variable)):
        sum += (firefly_b.variable[i] - firefly_a.variable[i]) ** 2
    return np.sqrt(sum)

class firefly:
    def __init__(self, variable, light):
        self.variable = variable
        self.light = light

class Fireflies:
    def __init__(self, alpha, beta, absorption, population, MaxGeneration, Value_Min, Value_Max):
        self.alpha = alpha
        self.beta = beta
        self.absorption = absorption
        self.population = population
        self.MaxGeneration = MaxGeneration
        self.Value_Min = Value_Min
        self.Value_Max = Value_Max
        self.fireflies = []
        self.coordinate = []
        self.brightness = 0

        for i in range(self.population):
            for j in range(len(self.Value_Min)):
                self.coordinate.append(random.uniform(self.Value_Min[j], self.Value_Max[j]))
            self.brightness = fn.targe_function(self.coordinate)
            self.fireflies.append(firefly(self.coordinate, self.brightness))
            self.coordinate = []
            self.brightness = 0

    def move(self, firefly_a, firefly_b):
        for i in range(len(self.Value_Min)):
            firefly_a.variable[i] += self.beta * np.exp(-self.absorption * ((distance(firefly_a, firefly_b)) ** 2)) * \
                                     (firefly_b.variable[i] - firefly_a.variable[i]) + self.alpha * (random.random() - 0.5)


def main():
    # standard = -1.8013
    starttime = datetime.datetime.now()
    Firefly = Fireflies(0.1, 1, 0.1, 60, 200, [0]*5, [np.pi]*5)

    most_light = float('inf')
    most_light_coordinate = np.zeros(len(Firefly.Value_Min))
    most_light_index = 0

    save_best_solution = np.zeros((Firefly.MaxGeneration, len(Firefly.Value_Min)+1)) #记录每一代结束后的全局最优解

    flag = 0

    t = 0
    while t < Firefly.MaxGeneration:

        # if np.abs(most_light - standard) < 0.0001 and flag == 0:
        #     endtime = datetime.datetime.now()
        #     flag = 1

        most_light_iter = float('inf')
        most_light_iter_coordinate = np.zeros(len(Firefly.Value_Min))

        # if t == 0:
        #     group_initial = np.zeros((Firefly.population, len(Firefly.Value_Min)))
        #     for i, firefly in enumerate(Firefly.fireflies):
        #         group_initial[i] = firefly.variable
        #     np.savetxt('initial.csv', group_initial, delimiter=',', fmt="%g")
        #
        # if t == 50:
        #     group_after50th = np.zeros((Firefly.population, len(Firefly.Value_Min)))
        #     for i, firefly in enumerate(Firefly.fireflies):
        #         group_after50th[i] = firefly.variable
        #     np.savetxt('after50th.csv', group_after50th, delimiter=',', fmt="%g")

        for i, firefly_i in enumerate(Firefly.fireflies):
            for j in range(i+1):
                I = Firefly.fireflies[j].light * np.exp(-Firefly.absorption*distance(firefly_i,Firefly.fireflies[j])**2)
                if firefly_i.light > I:  # j更亮
                    Firefly.move(firefly_i, Firefly.fireflies[j])
                firefly_i.light = fn.targe_function(firefly_i.variable)

            if firefly_i.light < most_light:
                most_light = firefly_i.light
                for m in range(len(Firefly.Value_Min)):
                    most_light_coordinate[m] = firefly_i.variable[m]
                most_light_index = t + 1

            if firefly_i.light < most_light_iter:
                most_light_iter = firefly_i.light
                for m in range(len(Firefly.Value_Min)):
                    most_light_iter_coordinate[m] = firefly_i.variable[m]

        Firefly.fireflies.sort(key=lambda firefly: firefly.light, reverse=False)

        save_best_solution[t] = np.insert(most_light_coordinate, 0, most_light) #完成一次迭代后获得目前为止的最优值

        print('iteration {} :  x*={}, f(x*)= {}'.format(t + 1, most_light_iter_coordinate, most_light_iter))
        print('best found at iteration {} :  x*={}, f(x*)= {}'.format(most_light_index, most_light_coordinate, most_light))
        t += 1

        # if t == Firefly.MaxGeneration:
        #     group_final = np.zeros((Firefly.population, len(Firefly.Value_Min)))
        #     for i, firefly in enumerate(Firefly.fireflies):
        #         group_final[i] = firefly.variable
        #     np.savetxt('final.csv', group_final, delimiter=',', fmt="%g")

    # np.savetxt('best_solution.csv', save_best_solution, delimiter=',', fmt="%g")
    # print(endtime - starttime)


if __name__ == "__main__":
    main()
