import numpy as np
import matplotlib.pyplot as plt

def newton(f, dfdx, x0, tol = 1e-10, max_itr = 50):
    x1 = x0 - 3 * f(x0) / dfdx(x0)
    if(np.abs(x0-x1) < tol):
        return [x1, [tol]]
    
    if(max_itr == 0):
        return [-1, [-1]]

    root = newton(f, dfdx, x1, tol, max_itr-1)


    errors = [x1 - root[0]]
    # print(f"newton error = {x1 - root}")
    errors.extend(root[1])
    return [root[0], errors]

def newton2(f, dfdx, x0, m=1, tol = 1e-10, max_itr = 50):
    x1 = x0 - 3 * (f(x0) / dfdx(x0))
    if(np.abs(x0-x1) < tol):
        return [[x1], [tol]]
    
    if(max_itr == 0):
        return [[x1], [tol]]

    root = newton2(f, dfdx, x1, m, tol, max_itr-1)

    errors = [x1 - root[0][-1]]
    errors.extend(root[1])

    xs = [x1]
    xs.extend(root[0])
    return [xs, errors]

def secant(f, x0, x1, tol= 1e-10, max_itr = 50):
    if(np.abs(x0-x1) < tol):
        return [x1, [tol]]
        
    
    if(max_itr == 0):
        return [-1, [-1]]
        

    fx1 = f(x1)
    fx0 = f(x0)

    x_next = x1 - fx1 / ((fx1 - fx0) / (x1 - x0))
    
    root = secant(f, x1, x_next, tol, max_itr-1)
    errors = [x1 - root[0]]
    errors.extend(root[1])


    return [root[0], errors]

def f(x):
    return np.exp(3 * x) - 27 * np.pow(x, 6) + 27 * np.pow(x, 4) * np.exp(x) - 9 * np.pow(x, 2) * np.exp(2 *x)

def dfdx(x):
    return 3 * np.exp(3 * x) - 162 * np.pow(x, 5) + (108 * np.pow(x, 3) * np.exp(x) + 27 * np.pow(x, 4) * np.exp(x)) - (18 * np.pow(x, 1) * np.exp(2 *x) + 18 * np.pow(x, 2) * np.exp(2 *x))

def d2fdx2(x):
    return 9 * np.exp(3 * x) - 810 * np.pow(x,4) + (324 * np.pow(x, 2) * np.exp(x) + 216 * np.pow(x, 3) * np.exp(x) + 27 * np.pow(x,4) * np.exp(x)) - (18 * np.exp(2 * x) + 72 * x * np.exp(2 * x) + 36  * np.pow(x, 2) * np.exp(2 * x))

def bad(x):
    return f(x) / dfdx(x)

def dbaddx(x):
    return 1 - (f(x) * d2fdx2(x) / np.pow(dfdx(x), 2))



print(dfdx(0))
print(dfdx(0.50829))
print(dfdx(0.91001))
print(dfdx(2.342))
print(dfdx(3.31602))
print(dfdx(3.73308))

sec = secant(f, 3.5, 3.8, max_itr=100)
n1 = newton2(f, dfdx, 3.5, max_itr=100)
n2 = newton(f, dfdx, 3.5, max_itr=100)
n3 = newton(bad, dbaddx, 3.5, max_itr=100)
print(sec[1])
print(n1)
# print(f"f({sec[0]}) = {f(sec[0])}")
# print(f"f({n1[0][-1]}) = {f(n1[0])}")
# print(f"f({n2[0][-1]}) = {f(n2[0])}")
# print(f"f({n3[0][-1]}) = {f(n3[0])}")
# # print(n3)

plt.plot(sec[0])
plt.plot(n1[0])
plt.plot(n2[0])
plt.plot(n3[0])
plt.show()

plt.plot(sec[1])
plt.plot(n1[1])
plt.plot(n2[1])
plt.plot(n3[1])
plt.show()

# print(f(newton(f, dfdx, 4, 1)[0]))
x = np.linspace(0,5, 1000)

plt.plot(x, f(x))
plt.plot(x, dfdx(x))
plt.plot(x, d2fdx2(x))
plt.ylim([-15, 15])
plt.show()