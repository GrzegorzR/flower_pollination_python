from random import random, sample
import numpy as np
from levy import get_levy_flight_array


class FPO:
    def __init__(self, obj_fun, iterations_num, pop_size,
                 p=0.5, dim=10, val_min = -100., val_max = 100):
        self.obj_fun = obj_fun
        self.iterations_num = iterations_num
        self.dim = dim
        self.pop_size = pop_size
        self.population = None
        self.best = (np.inf, None)
        self.p = p
        self.obj_vals = np.zeros(pop_size)
        self.val_max = val_max
        self.val_min = val_min

    def run(self):
        self.initialize_population()
        self.calculate_obj()
        for _ in range(self.iterations_num):
            self.check_best()
            self.pollination()
            print self.best[0]
        print self.best
    def initialize_population(self):
        self.population = [(np.random.rand(self.dim) * 200) - 100 for _ in range(self.pop_size)]

    def calculate_obj(self):
        for i, solution in enumerate(self.population):
            self.obj_vals[i] = self.obj_fun(solution)

    def check_best(self):
        if min(self.obj_vals) < self.best[0]:
            ind = np.argmin(self.obj_vals)
            self.best = (self.obj_vals[ind], self.population[ind])

    def pollination(self):
        for i in range(self.pop_size):
            if random() < self.p:
                self.global_pollination(i)
            else:
                self.local_pollination(i)

    def local_pollination(self, i):
        e = np.random.rand(self.dim)
        indexes = sample(range(0, self.pop_size), 2)
        sol1 = self.population[indexes[0]]
        sol2 = self.population[indexes[1]]
        tmp =  e* (sol1 + sol2)
        new_solution = self.population[i] + tmp
        self.check_new_solution(new_solution, i)

    def global_pollination(self, i):
        levy_vector = get_levy_flight_array(self.dim)
        tmp = levy_vector*(self.best[1] - self.population[i])
        new_solution = self.population[i] + tmp
        self.check_new_solution(new_solution, i)

    def check_new_solution(self, new_solution, i):
        if max(new_solution) < self.val_max and min(new_solution) > self.val_min:
            new_obj_val = self.obj_fun(new_solution)
            if new_obj_val < self.obj_vals[i]:
                self.population[i] = new_solution
                self.obj_vals[i] = new_obj_val