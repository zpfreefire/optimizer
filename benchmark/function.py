import numpy as np


def target_function(array):
    fitness = michalewicz(array)
    return fitness


'''benchmark functions'''


def ackley(array, a=20, b=0.2, c=2 * np.pi):
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


def alpine2(array):
    return np.sqrt(array[0]) * np.sqrt(array[1]) * np.sin(array[0]) * np.sin(array[1])


def bukin6(array):
    '''
    at d=2 : x1 ∈ [-15, 5]  x2 ∈ [-3, 3] , f([-10, 1]) = 0
    '''
    x1 = array[0]
    x2 = array[1]
    term1 = 100 * np.sqrt(abs(x2 - 0.01 * x1 ** 2))
    term2 = 0.01 * abs(x1 + 10)

    fitness = term1 + term2
    return fitness


def camel3(array):
    '''
    at d=2 : xi ∈ [-5, 5] , f([0,0]) = 0
    '''
    term1 = 2 * array[0] ** 2
    term2 = -1.05 * array[0] ** 4
    term3 = array[0] ** 6 / 6
    term4 = array[0] * array[1]
    term5 = array[1] ** 2

    fitness = term1 + term2 + term3 + term4 + term5
    return fitness


def camel6(array):
    '''
    at d=2 : x1 ∈ [-3, 3]  x2 ∈ [-2, 2], f([0.0898,-0.7126]) = f([-0.0898,0.7126]) = -1.0316284229280819
    '''
    term1 = (4 - 2.1 * array[0] ** 2 + (array[0] ** 4) / 3) * array[0] ** 2
    term2 = array[0] * array[1]
    term3 = (-4 + 4 * array[1] ** 2) * array[1] ** 2

    fitness = term1 + term2 + term3
    return fitness


def crossit(array):
    '''
    at d=2 : xi ∈ [-10, 10] , f([+/- 1.3491,+/- 1.3491]) = -2.0626118504479614
    '''
    term1 = np.sin(array[0]) * np.sin(array[1])
    term2 = np.exp(abs(100 - np.sqrt(array[0] ** 2 + array[1] ** 2) / np.pi))
    fitness = -0.0001 * (abs(term1 * term2) + 1) ** 0.1
    return fitness


def easom(array):
    '''
    at d=2 : xi ∈ [-100, 100] , f([np.pi,np.pi]) = -1
    '''
    term1 = -np.cos(array[0]) * np.cos(array[1])
    term2 = np.exp(-(array[0] - np.pi) ** 2 - (array[1] - np.pi) ** 2)
    fitness = term1 * term2
    return fitness


def eggholder(array):
    '''
    at d=2 : xi ∈ [-512, 512] , f([512,404.2319]) = -959.6406627106155
    '''
    z = - (array[1] + 47) * np.sin(np.sqrt(abs(array[1] + (array[0] / 2) + 47))) - array[0] * np.sin(
        np.sqrt(abs(array[0] - (array[1] + 47))))
    return z


def griewank(array):
    '''
    at d=2 : xi ∈ [-600, 600] , f([0.0,0.0]) = 0.0
    at d=5 : xi ∈ [-600, 600] , f([0.0,...,0.0]) = 0.0
    '''
    d = len(array)
    sum = 0
    prod = 1

    for i in range(1, d):
        xi = array[1]
        sum += xi ** 2 / 4000
        prod *= np.cos(xi / np.sqrt(i))
    fitness = sum - prod + 1
    return fitness


def holdertable(array):
    '''
    at d=2 : xi ∈ [-10, 10] , f([+/- 8.05502,+/- 9.66459]) = -19.208502567767606
    at d=5 : xi ∈ [-10, 10] , f([+/- 8.05502,...+/- 9.66459]) = -19.208502567767606
    '''
    term1 = np.sin(array[0]) * np.cos(array[1])
    term2 = np.exp(abs(1 - np.sqrt(array[0] ** 2 + array[1] ** 2) / np.pi))
    fitness = -abs(term1 * term2)
    return fitness


def levy(array):
    d = len(array)
    w = []
    for i in range(d):
        w[i] = 1 + (array[i] - 1) / 4

    term1 = (np.sin(np.pi * w[1])) ** 2
    term3 = (w[d] - 1) ** 2 * (1 + (np.sin(2 * np.pi * w[d])) ** 2)

    sum = 0
    for i in range(d - 2):
        wi = w[i]
        new = (wi - 1) ** 2 * (1 + 10 * (np.sin(np.pi * wi + 1)) ** 2)
        sum += new

    fitness = term1 + sum + term3
    return fitness


def levy13(array):
    '''
    at d=2 : xi ∈ [-10, 10] , f([1,1]) = 1.3497838043956716e-31
    '''
    term1 = (np.sin(3 * np.pi * array[0]) ** 2)
    term2 = (array[0] - 1) ** 2 * (1 + (np.sin(3 * np.pi * array[1])) ** 2)
    term3 = (array[1] - 1) ** 2 * (1 + (np.sin(2 * np.pi * array[1])) ** 2)

    fitness = term1 + term2 + term3
    return fitness


def michalewicz(array):  # for the number of Dimension is 2
    '''
    at d=2 : xi ∈ [0, π] , f([2.20,1.57]) = -1.801140718473825
    '''
    sum = 0
    fitness = 0
    m = 10
    for (i, x) in enumerate(array, start=1):
        sum = sum + np.sin(x) * np.sin((i * (x ** 2)) / np.pi) ** (2 * m)
    fitness = -sum
    return fitness


def rastrigin(array):
    '''
    at d=2 : xi ∈ [-5.12, 5.12] , f([0.0,0.0]) = 0.0
    at d=5 : xi ∈ [-5.12, 5.12] , f([0.0,...,0.0]) = 0.0
    :param array:
    :return:
    '''
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x ** 2 - 10 * np.cos(2 * np.pi * x)
    fitness = 10.0 * len(array) + sum
    return fitness


def rosenbrock(array):
    '''
    at d=2 : xi ∈ [-5, 10] , f([1,1]) = 0
    at d=5 : xi ∈ [-5, 10] , f([1,1,1,1,1]) = 0
    '''
    d = len(array)
    sum = 0
    for i in range(d - 1):
        xi = array[i]
        xnext = array[i + 1]
        new = 100 * (xnext - xi ** 2) ** 2 + (xi - 1) ** 2
        sum += new

    fitness = sum
    return fitness


def schaffer2(array):
    '''
    at d=2 : xi ∈ [-100, 100] , f([0,0]) = 0.0
    '''
    term1 = (np.sin(array[0] ** 2 - array[1] ** 2)) ** 2 - 0.5
    term2 = (1 + 0.001 * (array[0] ** 2 + array[1] ** 2)) ** 2

    fitness = 0.5 + term1 / term2
    return fitness


def schaffer4(array):
    term1 = np.cos(np.sin(abs(array[0] ** 2 - array[1] ** 2))) - 0.5
    term2 = (1 + 0.001 * (array[0] ** 2 + array[1] ** 2)) ** 2

    fitness = 0.5 + term1 / term2
    return fitness


def schwefel(array):
    '''
    at d=2 : xi ∈ [-500, 500] , f([420.9687,420.9687]) = 2.545567497236334e-05
    at d=5 : xi ∈ [-500, 500] , f([420.9687,...,420.9687]) = 6.363918737406493e-05
    '''
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x * np.sin(np.sqrt(np.abs(x)))
    fitness = 418.9829 * len(array) - sum
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


def sphere(array):
    '''
    at d=2 : xi ∈ [-5.12, 5.12] , f([0.0,0.0]) = 0.0
    at d=5 : xi ∈ [-5.12, 5.12] , f([0.0,...,0.0]) = 0.0
    '''
    fitness = 0
    for i in range(len(array)):
        fitness = fitness + array[i] ** 2
    return fitness


def stybtang(array):
    '''
        at d=2 : xi ∈ [-5, 5] , f([-2.903534,-2.903534]) = -78.3323314075428
        at d=5 : xi ∈ [-5, 5] , f([-2.903534,...,-2.903534) = -195.830828518857
    '''
    d = len(array)
    sum = 0
    for i in range(d):
        xi = array[i]
        new = xi ** 4 - 16 * xi ** 2 + 5 * xi
        sum += new

    fitness = sum / 2

    return fitness

# print(ackley([0,0,0,0,0]))
# print(alpine2())                       未测
# print(bukin6([-10, 1]))
# print(camel3([0,0]))
# print(camel6([-0.0898, 0.7126]))
# print(crossit([-1.3491, -1.3491, -1.3491, -1.3491, -1.3491]))
# print(easom([np.pi,np.pi]))
# print(eggholder([512, 404.2319]))
# print(griewank([0, 0, 0, 0, 0]))
# print(holdertable([8.05502, 9.66459]))
# print(levy([1,1]))                     error
# print(levy13([1,1]))
# print(michalewicz([2.2, 1.57]))
# print(rastrigin([0, 0, 0, 0, 0]))
# print(rosenbrock([1,1,1,1,1]))
# print(schaffer2([0,0]))
# print(schaffer4([]))                   error 没有给极值和x*取值
# print(schwefel([420.9687, 420.9687, 420.9687, 420.9687, 420.9687]))
# print(shubert([]))                    error x*没有给取值
# print(sphere([0, 0, 0, 0, 0]))
# print(stybtang([-2.903534, -2.903534, -2.903534, -2.903534, -2.903534]))
