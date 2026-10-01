import numpy as np
import matplotlib.pyplot as plt

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

def newton(f, dfdx, x0, tol = 1e-10, max_itr = 50):
    x1 = x0 - f(x0) / dfdx(x0)
    if(np.abs(x0-x1) < tol):
        return [x1, [tol]]
    
    if(max_itr == 0):
        return [-1, [-1]]

    root = newton(f, dfdx, x1, tol, max_itr-1)


    errors = [x1 - root[0]]
    # print(f"newton error = {x1 - root}")
    errors.extend(root[1])
    return [root[0], errors]

def f(x):
    return np.pow(x,6) - x -1

def dfdx(x):
    return 6 * np.pow(x,5)- 1


newtons = newton(f, dfdx, 2)
sec = secant(f, 1, 2)
print(sec[1])

xk = np.abs(np.array(newtons[1][0:-2]))
xkplus = np.abs(np.array(newtons[1][1:-1]))

plt.loglog(xk, xkplus)

xk = np.abs(np.array(sec[1][0:-2]))
xkplus = np.abs(np.array(sec[1][1:-1]))
plt.loglog(xk, xkplus)
plt.xlabel("error of x_n")
plt.ylabel("error of x_n+1")

plt.show()