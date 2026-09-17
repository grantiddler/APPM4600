"""
 This script uses the bisection method to approximate the root of a 
 scalar function.
"""

############################################# 
"""
Copyright (C) 2025  Adrianna M. Gillman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
############################################# 

# import libraries
import numpy as np
import matplotlib.pyplot as plt

def driver():

# use routines    
    f = lambda x: x - 4 * np.sin(2 * x) - 3
    a = 1
    b = 4

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-10

    x = np.linspace(-1, 7, 200)
    plt.plot(x, f(x))
    plt.plot([-1,7], [0,0])
    plt.show()
    plt.plot(x, x- f(x) )
    plt.plot(x, x)


    [fp, count] = fixedpoint2(f,1,tol)
    print('the approximate root is',fp)
    print(f"found in {count} iterations")
    print('f(fp) =', f(fp))


# define routines
def fixedpoint(f, x0, tol, itr = 0,  nmax = 100):
    x1 = f(x0)
    plt.plot(x0, x1, 'o', color='black')
    
    # input(f"{x0}, {x1}")
    

    if(np.abs(x0 - x1) <= tol or nmax < itr):
        return([x1, itr])
    else:
        return fixedpoint(f, x1, tol, itr + 1, nmax)


def fixedpoint2(f, x0, tol, itr = 0,  nmax = 100):
    x1 = - np.sin(2 * x0) + (5 * x0 / 4) - (3/4)

    if(np.abs(x0 - x1) <= tol or nmax < itr):
        plt.show()
        return([x1, itr])
        
    else:
        plt.plot(x0,x1,'o')

        return fixedpoint2(f, x1, tol, itr + 1, nmax)
      
driver()               


