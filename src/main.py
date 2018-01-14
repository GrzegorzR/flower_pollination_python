from FPO import FPO
from test_functions import *

test_functions = [cigar, rosenberg, rastrigin, zakharov]


def main():
    test_fun = test_functions[1]
    iterations_number = 501
    population_size = 50
    p = 0.8
    fpo = FPO(test_fun, iterations_number, population_size, p=p, plot=True)
    fpo.run()


if __name__ == "__main__":
    main()
