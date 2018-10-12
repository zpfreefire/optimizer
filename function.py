import numpy as np


def targe_function(array):
    pass


'''benchmark functions'''

''' input domain:   x*=[-32.768, 32.768] 
    global minimum: f(x*)=0,x*=(0,0,...0)'''


def ackley(array, a=20, b=0.2, c=2 * np.pi):
    d = len(array)

    sum1 = 0
    sum2 = 0
    for i in range(1, d - 1):
        xi = array[i]
        sum1 = sum1 + xi ** 2
        sum2 = sum2 + np.cos(c * xi)
    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)

    fitness = term1 + term2 + a + np.exp(1)

    return fitness


def alpine2(array):
    return np.sqrt(array[0]) * np.sqrt(array[1]) * np.sin(array[0]) * np.sin(array[1])


def bukin6(array):
    x1 = array[0]
    x2 = array[1]
    term1 = 100 * np.sqrt(abs(x2 - 0.01 * x1 ** 2))
    term2 = 0.01 * abs(x1 + 10)

    fitness = term1 + term2
    return fitness


def camel3(array):
    term1 = 2 * array[0] ** 2
    term2 = -1.05 * array[0] ** 4
    term3 = array[0] ** 6 / 6
    term4 = array[0] * array[1]
    term5 = array[1] ** 2

    fitness = term1 + term2 + term3 + term4 + term5
    return fitness


def camel6(array):
    term1 = (4 - 2.1 * array[0] ** 2 + (array[0] ** 4) / 3) * array[0] ** 2
    term2 = array[0] * array[1]
    term3 = (-4 + 4 * array[1] ** 2) * array[1] ** 2

    fitness = term1 + term2 + term3
    return fitness


def crossit(array):
    term1 = np.sin(array[0]) * np.sin(array[1])
    term2 = np.exp(abs(100 - np.sqrt(array[0] ** 2 + array[1] ** 2)) / np.pi)
    fitness = -0.0001 * (abs(term1 * term2) + 1) ** 0.1
    return fitness


def holdertable(array):
    term1 = np.sin(array[0]) * np.cos(array[1])
    term2 = np.exp(abs(1 - np.sqrt(array[0] ** 2 + array[1] ** 2)) / np.pi)
    fitness = -abs(term1 + term2)
    return fitness


def easom(array):
    term1 = -np.cos(array[0]) * np.cos(array[1])
    term2 = np.exp(-(array[0] - np.pi) ** 2 - (array[1] - np.pi) ** 2)
    fitness = term1 + term2
    return fitness


def rosenbrock(array):
    d = len(array)
    sum = 0
    for i in range(d - 1):
        xi = array[i]
        xnext = array[i + 1]
        new = 100 * (xnext - xi * 2) ** 2 + (xi - 1) ** 2
        sum += new

    fitness = sum
    return fitness


def shubert(array):
    sum1 = 0
    sum2 = 0
    for i in range(1, 5):
        new1 = i * np.cos((i + 1) * array[0] + i)
        new2 = i * np.cos((i + 1) * array[1] + i)
        sum1 += new1
        sum2 += new2

    fitness = sum1 * sum2
    return fitness


def stybtang(array):
    d = len(array)
    sum = 0
    for i in range(1, d):
        xi = array[i]
        new = xi ** 4 - 16 * xi ** 2 + 5 * xi
        sum += new

    fitness = sum / 2

    return fitness


def griewank(array):
    d = len(array)
    sum = 0
    prod = 1

    for i in range(1, d):
        xi = array[1]
        sum += xi ** 2 / 4000
        prod *= np.cos(xi / np.sqrt(i))
    fitness = sum - prod + 1
    return fitness


def levy(array):
    d = len(array)
    w = []
    for i in range(1, d):
        w[i] = 1 + (array[i] - 1) / 4

    term1 = (np.sin(np.pi * w[1])) ** 2
    term3 = (w[d] - 1) ** 2 * (1 + (np.sin(2 * np.pi * w[d])) ** 2)

    sum = 0
    for i in range(1, d - 1):
        wi = w[i]
        new = (wi - 1) ** 2 * (1 + 10 * (np.sin(np.pi * wi + 1)) ** 2)
        sum += new

    fitness = term1 + sum + term3
    return fitness


def levy13(array):
    term1 = (np.sin(3 * np.pi * array[0]) ** 2)
    term2 = (array[0] - 1) ** 2 * (1 + (np.sin(3 * np.pi * array[1])) ** 2)
    term3 = (array[1] - 1) ** 2 * (1 + (np.sin(2 * np.pi * array[1])) ** 2)

    fitness = term1 + term2 + term3
    return fitness


def schaffer2(array):
    term1 = (np.sin(array[0] ** 2 - array[1] ** 2)) ** 2 - 0.5
    term2 = (1 + 0.001 * (array[0] ** 2 + array[1] ** 2)) ** 2

    fitness = 0.5 + term1 / term2
    return fitness


def schaffer4(array):
    term1 = np.cos(np.sin(abs(array[0] ** 2 - array[1] ** 2))) - 0.5
    term2 = (1 + 0.001 * (array[0] ** 2 + array[1] ** 2)) ** 2

    fitness = 0.5 + term1 / term2
    return fitness


def eggholder(array):
    z = - (array[1] + 47) * np.sin(np.sqrt(abs(array[1] + (array[0] / 2) + 47))) - array[0] * np.sin(
        np.sqrt(abs(array[0] - (array[1] + 47))))
    return z


def sphere(array):
    fitness = 0
    for i in range(len(array)):
        fitness = fitness + array[i] ** 2
    return fitness


def rastrigin(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x ** 2 - 10 * np.cos(2 * np.pi * x)
    fitness = 10.0 * len(array) + sum
    return fitness


def schwefel(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x * np.sin(np.sqrt(np.abs(x)))
    fitness = 418.9829 * len(array) - sum
    return fitness


def michalewicz(array):  # for the number of Dimension is 2
    sum = 0
    fitness = 0
    m = 10
    for (i, x) in enumerate(array, start=1):
        sum = sum + np.sin(x) * np.sin((i * (x ** 2)) / np.pi) ** (2 * m)
    fitness = -sum
    return fitness
