import matplotlib.pyplot as plt
from numba import jit
import numpy as np

def zeta_over_eta(x, y):
    X = -2**(1-x)
    Y = 2**(1j*y)
    return Y/(X+Y)

# @jit(nopython=True)
def zeta(x, y):
    term = 5*10**4
    re = 0.0
    im = 0.0
    for i in range(1, term):
        b = y*np.log(i)
        A = (-1)**(i-1)/i**x
        re += A * np.cos(b)
        im += A * np.sin(b)
    eta = re - im*1j
    X = -2**(1-x)
    Y = 2**(1j*y)
    u = (Y/(X+Y))*eta
    return u
a = float(input("give the domain of complex numbers: "))
b = float(input("give the real part of the complex number : "))
im = np.linspace(1, a, 2000)
re = 0.5*np.ones(2000)
value = zeta(b, im)
real = value.real
imaginary = value.imag
plt.plot(real, imaginary)
plt.show()