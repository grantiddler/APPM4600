import numpy as np
import matplotlib.pyplot as plt

delta = np.pow(10.0,np.arange(-16, 0, .1))



x1 = 1
x2 = np.pi

def f1(x, delta):
    return np.cos(x + delta) - np.cos(x)

def f2(x, delta):
    return -2 * np.sin(x + delta/2) * np.sin(delta/2)

def f3(x, delta):
    return - delta * np.sin(x) - np.pow(delta, 2) * np.cos(x + delta/2) / 2

plt.semilogx(delta, f1(x1,delta) - f2(x1,delta))
plt.semilogx(delta, f1(x2,delta) - f2(x2,delta))
plt.show()

plt.semilogx(delta, f1(x1,delta) - f2(x1,delta))
plt.semilogx(delta, f1(x2,delta) - f2(x2,delta))
plt.show()


plt.semilogx(delta, f2(x2,delta) - f3(x2,delta))
plt.semilogx(delta, f2(x1,delta) - f3(x1,delta))
plt.show()
