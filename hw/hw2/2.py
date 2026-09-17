import numpy as np
from scipy.linalg import norm

a = np.array([[1, 1], [1 +1e-10, 1-1e-10]])
ainv = np.array([[1 - 1e10, 1e10], [1 +1e10, 1e10]])
print(a)
print(ainv)

print(norm(a))
print(norm(ainv))