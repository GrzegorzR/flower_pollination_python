import numpy as np


def _phi(alpha, beta):
    """ Common function. """
    return beta * np.tan(np.pi * alpha / 2.0)


def change_par(alpha, beta, mu, sigma, par_input, par_output):
    if par_input == par_output:
        return mu
    elif (par_input == 0) and (par_output == 1):
        return mu - sigma * _phi(alpha, beta)
    elif (par_input == 1) and (par_output == 0):
        return mu + sigma * _phi(alpha, beta)


def random_levy(alpha, beta, mu=0.0, sigma=1.0, shape=(), par=0):
    loc = change_par(alpha, beta, mu, sigma, par, 0)
    if alpha == 2:
        return np.random.standard_normal(shape) * np.sqrt(2.0)

    radius = 1e-15
    if np.absolute(alpha - 1.0) < radius:
        alpha = 1.0 + radius

    r1 = np.random.random(shape)
    r2 = np.random.random(shape)
    pi = np.pi

    a = 1.0 - alpha
    b = r1 - 0.5
    c = a * b * pi
    e = _phi(alpha, beta)
    f = (-(np.cos(c) + e * np.sin(c)) / (np.log(r2) * np.cos(b * pi))) ** (a / alpha)
    g = np.tan(pi * b / 2.0)
    h = np.tan(c / 2.0)
    i = 1.0 - g ** 2.0
    j = f * (2.0 * (g - h) * (g * h + 1.0) - (h * i - 2.0 * g) * e * 2.0 * h)
    k = j / (i * (h ** 2.0 + 1.0)) + e * (f - 1.0)
    return loc + sigma * k


def get_levy_flight_array(dim=10):
    return np.array([abs(random_levy(1.5, 0)) for _ in range(dim)])


if __name__ == "__main__":

    for i in range(100):
        print random_levy(1.5, 0)
