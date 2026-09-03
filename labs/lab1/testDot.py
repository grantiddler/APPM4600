"""
This program is a warm up for coding. You get used to the coding
format and practice some coding skills.
"""
#############################################
"""
Copyright (C) 2025 Adrianna M. Gillman
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
#############################################
import numpy as np
import numpy.linalg as la
import math

def driver():
    n = 100
    x = np.linspace(0,np.pi,n)
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    f = lambda x: np.sin(2 * x)
    g = lambda x: np.sin(x)
    y = f(x)
    w = g(x)


    dp = dotProduct(y,w,n)
    # print the output
    print('the dot product is : ', dp)


    A = np.array([[1,2],[3,4]])
    B = np.array([[1],[0]])

    print(matrixProduct(A,B))
    return

def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0
    for j in range(n):
        dp = dp + x[j]*y[j]

    return dp

def matrixProduct(A,B):
    if (np.shape(A)[1] != np.shape(B)[0]):
        return None

    m = np.shape(A)[0]
    l = np.shape(A)[1]

    n = np.shape(B)[1]
    C = np.zeros((m, n))


    for i in range(m):
        for j in range(n):

            C[i, j] = dotProduct(A[i, :], B[:, j], l)



    return C

driver()