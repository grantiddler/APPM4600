import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.pow(x,9) - 18 * np.pow(x, 8) + 144 * np.pow(x, 7) - 672 * np.pow(x, 6) +2016 * np.pow(x, 5) - 4032 * np.pow(x, 4) + 5376 * np.pow(x, 3) - 4608 * np.pow(x,2) + 2304 * x- 512

def f2(x):
    return np.pow(x-2, 9)


x = np.arange(1.92, 2.08, .001)
print(x)

plt.plot(x,f1(x))
plt.plot(x,f2(x))
plt.show()