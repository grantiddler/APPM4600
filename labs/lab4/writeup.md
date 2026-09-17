# prelab



# 1
g(x) = x - f(x)/f'(x)

|g'(x)| < 1 guarantees unique convergence

# 2
see code

# 3
the new function needs f(x), f'(x), and f''(x) to determine when it has reached the basin of convergence for newtons method

# 4
see code

# 5
the new function needs f(x), f'(x), and f''(x), but can evaluate functions outside of the basin of convergence for newtons method
and also seperate tolerances and max iterations for bisection and newtons method

# 6

f(x) = e^(x^2 + 7x - 30) - 1
f'(x) = (2x + 7) * e^(x^2 + 7x - 30)
f''(x) = (4x^2 + 28x + 51) * e^(x^2 + 7x - 30)


newtons method finished in 26 iterations
the bisection method finished in 35 iterations
the hybrid method finished in 8 iterations

The hybrid method finished the fastest 