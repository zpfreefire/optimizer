import numpy as np
import random

import function as fn


class waterWave():
    def __init__(self, minbounds, maxbounds, hmax, alpha, beta, A, kmax, WaveNum, iteration):
        self.minbounds = minbounds
        self.maxbounds = maxbounds
        self.hmax = hmax
        self.alpha = alpha
        self.beta = beta
        self.A = A
        self.kmax = kmax
        self.WaveNum = WaveNum
        self.Popu = []
        self.popution = []
        self.h = []
        self.WaveLen = []
        self.maxFitness = 0.0
        self.minFitness = 0.0
        self.BestWave = []
        self.BestValue = []
        self.iteration = iteration
        self.para = 0.001
        self.InitPopu(self.minbounds, self.maxbounds)

    def InitPopu(self, minbounds, maxbounds):
        temp = []
        for i in range(self.WaveNum):
            for j in range(len(minbounds)):
                for z in range(len(maxbounds)):
                    if j == z:
                        temp.append(random.uniform(minbounds[j], maxbounds[z]))
            self.popution.append(temp)
            self.h.append(self.hmax)
            self.WaveLen.append(self.A)
            temp = []
        return self.popution
        # print(self.popution)

    def Propagation(self, popu, num, minbounds, maxbounds):
        self.Popu = []
        for i in range(len(minbounds)):
            for j in range(len(maxbounds)):
                if i == j:
                    temp = popu[i] + random.uniform(-1, 1) * self.WaveLen[num] * (maxbounds[j] - minbounds[i])
                    while temp < minbounds[i] or temp > maxbounds[j]:
                        temp = popu[i] + random.uniform(-1, 1) * self.WaveLen[num] * (maxbounds[j] - minbounds[i])
                    self.Popu.append(temp)
                else:
                    pass
        return self.Popu

    def Refaction(self, population, popu, num):
        self.Popu = []
        temp = self.getBest(population)
        for i in range(len(temp)):
            for j in range(len(popu)):
                if i == j:
                    flag = np.random.normal((popu[j] + temp[i]) / 2, np.abs(temp[i] - popu[j]) / 2)
                    self.Popu.append(flag)
        self.h[num] = self.hmax
        if (self.CostFunction(self.Popu) == 0):
            pass
        else:
            self.WaveLen[num] = self.WaveLen[num] * self.CostFunction(self.popution[num]) / self.CostFunction(self.Popu)
        return self.Popu

    def Breaking(self, popu, minbounds, maxbounds):
        self.Popu = []
        for i in range(len(minbounds)):
            for j in range(len(maxbounds)):
                if i == j:
                    temp = popu[i] + np.random.normal(0, 1) * self.beta * (maxbounds[j] - minbounds[i])
                    self.Popu.append(temp)
        return self.Popu
        # print(self.Popu)

    def CostFunction(self, X):
        return fn.target_function(X)
        # Booth Function
        # Cost =(X[0] + 2 * X[1] - 7) ** 2 + (2 * X[0] + X[1] - 5) ** 2
        # Michalewicz function
        # sum = 0
        # Cost = 0
        # m = 10
        # for (i, x) in enumerate(X, start=1):
        # sum = sum + np.sin(x) * np.sin((i * (x ** 2)) / np.pi) ** (2 * m)
        # Cost = -sum
        # Matyas Function
        # sum=0
        # Cost=0
        # for (i,x) in enumerate(X,start=1):
        # sum=sum+0.26*(i**2+x**2)-0.48*i*x
        # Cost=sum
        # RosenBrock Function
        # sum=0
        # Cost=0
        # for (i,x) in enumerate(X,start=1):
        # sum =sum + 100 * ((x - i ** 2) ** 2) + (i - 1) ** 2
        # Cost=sum
        # return Cost

    def getMaxFitness(self, population):
        self.maxFitness = self.CostFunction(population[0])
        for i in range(len(population)):
            if (self.CostFunction(population[i]) > self.maxFitness):
                self.maxFitness = self.CostFunction(population[i])
        return self.maxFitness
        # print(self.maxFitness)

    def getMinFitness(self, population):
        self.minFitness = self.CostFunction(population[0])
        for i in range(len(population)):
            if (self.CostFunction(population[i]) < self.minFitness):
                self.minFitness = self.CostFunction(population[i])
        return self.minFitness
        # print(self.minFitness)

    def getBest(self, population):
        self.BestWave = []
        self.minFitness = self.CostFunction(population[0])
        flag = 0
        for i in range(len(population)):
            if (self.CostFunction(population[i]) < self.minFitness):
                self.minFitness = self.CostFunction(population[i])
                flag = i
        Best = population[flag]
        for i in range(len(Best)):
            self.BestWave.append(Best[i])
        return self.BestWave

    def waterWave_search(self):
        t = 1
        while t <= self.iteration:
            for i in range(len(self.popution)):
                Temp = self.Propagation(self.popution[i], i, self.minbounds, self.maxbounds)
                if self.CostFunction(Temp) < self.CostFunction(self.popution[i]):
                    if self.CostFunction(Temp) < self.CostFunction(self.getBest(self.popution)):
                        self.BestValue = []
                        temp = self.Breaking(Temp, self.minbounds, self.maxbounds)
                        for j in range(len(temp)):
                            self.BestValue.append(temp[j])
                    self.popution[i] = Temp
                else:
                    self.h[i] -= 1
                    if self.h[i] == 0:
                        temp = self.Refaction(self.popution, self.popution[i], i)
                        self.popution[i] = temp
            print("Iteration: ", t, "Fitness: ", self.CostFunction(self.getBest(self.popution)))
            self.BestValue = []
            flag = self.getBest(self.popution)
            for j in range(len(flag)):
                self.BestValue.append(flag[j])
            for i in range(len(self.popution)):
                self.WaveLen[i] = self.WaveLen[i] * self.alpha ** (
                        -(self.CostFunction(self.popution[i]) - self.getMinFitness(self.popution) + self.para)
                        / (self.getMaxFitness(self.popution) - self.getMinFitness(self.popution) + self.para))
            t += 1
        for k in range(len(self.BestValue)):
            print("%.4f" % self.BestValue[k])


if __name__ == "__main__":
    test = waterWave([0] * 16, [np.pi] * 16, 6, 1.026, 0.001, 0.5, 1, 50, 200)
    test.waterWave_search()
