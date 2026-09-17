import numpy as np
import math

def f(x):
    return np.exp(x) - 1
    
def estimate(x):
    y = 0
    for i in range(1,14):
        y += np.pow(x,i) / math.factorial(i)

    return y

x = 9.999999995000000e-10



print(estimate(x))
