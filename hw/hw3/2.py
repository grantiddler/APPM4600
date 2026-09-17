from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt


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

      
      
def integrand(s):
    return np.exp(-(s ** 2)) 

def erf(t):
    integral = quad(integrand,0, t)[0]


    return 2 * integral / np.sqrt(np.pi)

def T(x, t):
	Ts = -15
	Ti = 20
	alpha = 0.138e-6
	vec_erf = np.vectorize(erf)
	return vec_erf( x / (2 * np.sqrt(alpha * t))) * (Ti - Ts) + Ts

def f(x):
    return T(x, 60)

def dfdx(x):
	Ts = -15
	Ti = 20
	alpha = 0.138e-6
	t = 60
	return np.exp( - np.pow(x, 2) / (4 * alpha * t)) * (Ti-Ts) / (2 * np.sqrt(alpha * t * np.pi))

# def newton(f, dfdx, x0, tol= 1e-10, itr = 50):
# 	if(dfdx(x0) == 0):
# 		print(f"newtons method fails df/dx({x0}) = {dfdx(x0)}")
# 		return np.nan
	
# 	plt.plot(x0, f(x0), 'o', color="black")

# 	x1 = x0 - (f(x0) / dfdx(x0))
# 	print(x1)

# 	if np.abs(x1 - x0) < tol or itr == 0:
# 		return x1


# 	return newton(f, dfdx, x1, tol, itr - 1)

# def newton(f,fp,p0,tol,Nmax):
# 	"""
# 	Newton iteration.

# 	Inputs:
# 	f,fp - function and derivative
# 	p0   - initial guess for root
# 	tol  - iteration stops when p_n,p_{n+1} are within tol
# 	Nmax - max number of iterations
# 	Returns:
# 	p     - an array of the iterates
# 	pstar - the last iterate
# 	info  - success message
# 			- 0 if we met tol
# 			- 1 if we hit Nmax iterations (fail)
		
# 	"""
# 	p = np.zeros(Nmax+1);
# 	p[0] = p0
# 	for it in range(Nmax):
# 		p1 = p0-f(p0)/fp(p0)

# 		plt.plot(p0, f(p0), 'o')
# 		p[it+1] = p1
# 		if (abs(p1-p0) < tol):
# 			pstar = p1
# 			info = 0
			
# 			return [p,pstar,info,it]
# 		p0 = p1
# 	pstar = p1
# 	info = 1
# 	return [p,pstar,info,it]





print(bisection(f, 0, .1, 1e-10))
print(newton(f, dfdx, 0.002, 1e-10, 1000))
# print(newton(f, dfdx, 0.001))

x = np.linspace(-1,1, 100)
plt.plot(x, f(x))
plt.show()
