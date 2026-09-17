import numpy as np


def a(x0, tol=1/10**10, itr = 50):
    x1 = -16 + 6 * x0 + 12 / x0
    print(x0)
    if np.abs(x1 - x0) < tol or itr <= 0:
        return x1
    return a(x1, tol, itr - 1)

def b(x0, tol=1/10**10, itr = 50):
    x1 = x0 * 2 / 3  + 1 / (x0 ** 2)
    print(x0)
    if np.abs(x1 - x0) < tol or itr <= 0:
        return x1
    return b(x1, tol, itr - 1)

def c(x0, tol=1/10**10, itr = 50):
    x1 = 12 / (1 + x0)
    print(x0)
    if np.abs(x1 - x0) < tol or itr <= 0:
        return x1
    return c(x1, tol, itr - 1)

b(4)
c(4)
