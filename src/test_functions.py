from math import cos, pi


def cigar(x):
    tmp1 = x[0] ** 2.
    tmp2 = 0.
    for xi in x[1:]:
        tmp2 += xi ** 2

    return tmp1 + ((10. ** 6.) * tmp2)


def rosenberg(x):
    result = 0.
    for i in range(len(x) - 1):
        result += (100. * ((x[i] ** 2) - x[i + 1]) ** 2) + ((x[i] - 1) ** 2)
    return result


def rastrigin(x):
    result = 0.
    for xi in x:
        result += ((xi ** 2) - (10. * cos(2. * pi * xi)) + 10.)
    return result

def zakharov(x):
    tmp1 = 0.
    x_sum = sum(x)
    for xi in x:
        tmp1 += xi ** 2
    tmp2 = (0.5 * x_sum) ** 2
    tmp3 = (0.5 * x_sum) ** 4
    return tmp1 + tmp2 + tmp3
