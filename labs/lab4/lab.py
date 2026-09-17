import numpy as np

def f(x):
    return np.exp(np.pow(x, 2) + 7 * x - 30) - 1

def dfdx(x):
    return (2 * x + 7) * np.exp(np.pow(x, 2) + 7 * x - 30)

def d2fdx2(x):
    return (4 * np.pow(x, 2) + 28 * x + 51) * np.exp(np.pow(x, 2) + 7 * x - 30)

def g(x):
    return x - f(x) / dfdx(x)

def dgdx(x): 
    return f(x) * d2fdx2(x) / np.pow(dfdx(x), 2)

def bisection2(a, b, tol = 1e-10, max_itr = 50, itr = 0):
    c = (a + b) / 2

    if np.abs(dgdx(c)) < 1:
        print(f"x0 = {c} - switching to newton after {itr} iterations")
        return newton(c, tol)

    if  itr == 0:
        return c

    fa = f(a)
    fb = f(b)
    fc = f(c)

    if fa == 0:
        return a
    elif fb == 0:
        return b
    elif fa * fc > 0:
        return bisection2(c, b, tol, max_itr, itr + 1)
    elif fb * fc > 0:
        return bisection2(a, c, tol, max_itr, itr + 1)

def bisection(a, b, tol = 1e-10, max_itr = 50, itr = 0):
    c = (a + b) / 2

    if np.abs(a - b) < tol or itr == max_itr:
        return [c, itr]


    fa = f(a)
    fb = f(b)
    fc = f(c)

    if fa == 0:
        return a
    elif fb == 0:
        return b
    elif fa * fc > 0:
        return bisection(c, b, tol, max_itr, itr + 1)
    elif fb * fc > 0:
        return bisection(a, c, tol, max_itr, itr + 1)
    
def newton(x0, tol, max_itr = 50, itr = 0):
    x1 = g(x0)
    if(np.abs(x1 - x0) < tol) or itr == max_itr:
        return [x1, itr]
    return newton(x1, tol, max_itr, itr + 1)


a = bisection2(2, 4.5, 1e-10)
b = bisection(2, 4.5, 1e-10)
c = newton(4.5, 1e-10)

print(f"newtons method finished in {c[1]} iterations")
print(f"the bisection method finished in {b[1]} iterations")
print(f"the hybrid method finished in {a[1]} iterations")