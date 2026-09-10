import numpy as np
import matplotlib.pyplot as plt
    


def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    arr = [x0]
    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       arr.append(x1)

       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return arr
       x0 = x1

    xstar = x1
    ier = 1
    return arr


def aitkin(p):
    x = []
    for n in range(len(p) - 2):
        phatn =  p[n] - np.pow(p[n+1] - p[n], 2) / (p[n + 2] - 2 * p[n+1] + p[n])
        x.append(phatn)
    return x


def alpha(a,b,c, d):
    return np.log(np.abs((a - d) / (b - d))) / np.log(np.abs((b - d) / (c - d)))

Nmax = 100
tol = 1e-7

g = lambda x: np.sqrt(10 / (x + 4))

p = fixedpt(g,1.5,tol,Nmax)

plt.plot(p)
plt.show()

print(alpha(p[-3], p[-2], p[-1], 1.3652300134140976))

p = aitkin(p)
plt.plot(p)
plt.show()

print(alpha(p[-3], p[-2], p[-1], 1.3652300134140976))