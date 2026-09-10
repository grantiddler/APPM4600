
# import libraries
import numpy as np
import matplotlib.pyplot as plt
    
def driver():

    # test functions 
    f1 = lambda x: 1+0.5*np.sin(x)
    # fixed point is alpha1 = 1.4987....

    f2 = lambda x: 3+2*np.sin(x)

    g = lambda x: np.sqrt(10 / (x + 4))
    #fixed point is alpha2 = 3.09... 

    Nmax = 100
    tol = 1e-6


    x0 = 0.0
    print(fixedpt(g,x0,tol,Nmax)[-1])

    plt.plot(fixedpt(g,1.5,tol,Nmax))
    plt.show()


# define routines
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
    
def alpha(a,b,c):
    return np.log(np.abs(a * b)) / np.log(np.abs(b / c))
driver()