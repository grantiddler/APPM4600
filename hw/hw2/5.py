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
    f = lambda x: x**3 + x - 4
    a = 1
    b = 4

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-3

    [astar,count] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print(f"found in {count} iterations")
    print('f(astar) =', f(astar))


# define routines
def bisection(f,a,b,tol, itr = 0):
	d = (a + b) / 2

	fa = f(a)
	fb = f(b)
	fd = f(d)
	if(fa * fb > 0):
		return -1

	elif(fa == 0):
		return [a, itr]
	elif(fb == 0):
		return [b, itr]

	elif(b - a < tol):
		return [d, itr]
	elif(fa * fd > 0):
		return bisection(f, d, b, tol, itr + 1)
	else:
		return bisection(f,a,d, tol, itr + 1)

      
driver()               


