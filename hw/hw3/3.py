import numpy as np
def fa(x):
    return x * ((1 + (7 - (x ** 5)) / (x ** 2)) ** 3)

def a(x0, tol=1/10**10, itr = 50):
    x1 = fa(x0)
    print(x0)
    if np.abs(x1 - x0) < tol or itr <= 0:
        return x1
    return a(x1, tol, itr - 1)

def fb(x):
    return x - (x ** 5 - 7) / (x ** 2)

def b(x0, tol=1/10**10, itr = 50):
    x1 = fb(x0)
    print(x0)
    if np.abs(x1 - x0) < tol or itr <= 0:
        return x1
    return b(x1, tol, itr - 1)


def fc(x):
    return x - (x ** 5 - 7) / (4 * x ** 4)

def c(x0, tol=1/10**10, itr = 50):
    x1 = fc(x0)
    if np.abs(x1 - x0) < tol or itr <= 0:
        return x1
    return c(x1, tol, itr - 1)

def fd(x):
    return x - (x ** 5 - 7) / 12

def d(x0, tol=1/10**10, itr = 50):
    x1 = fd(x0)
    if np.abs(x1 - x0) < tol or itr <= 0:
        return x1
    return d(x1, tol, itr - 1)



# print(a(1))
print(b(1))
print(c(1))
print(d(1))

print(np.pow(7, 1/5))