import numpy as np
import matplotlib.pyplot as plt

# 3.2.1
x = np.linspace(1,1.9,10)
y = np.arange(1,2,.1)

# 3.2.2, 3.2.3
print(f"the first 3 entries of x are {x[0:3]}")

#3.2.4
w = 10**(-np.linspace(1,10,10))
x = np.linspace(1,10,10)
print(w)

plt.semilogy(x,w)

plt.show()

#3.2.5
s = 3 * w


plt.semilogy(x,w)
plt.semilogy(x,s)

plt.show()