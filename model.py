from math import factorial, pi
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm

# Note: np math functions hve to be used when involving ndarrays (r, theta, phi)

# 4.3 #
# constants
Z = 1                           # proton number
a0 = Z * 0.528 * 10**-10   # reduced Bohr radius

# derivative generation

def ordered_derivative(f, n):
    """ Calculates the nth-powered derivative of function f. """

    dx = 1e-5
    derivative = lambda x: (f(x+dx) - f(x)) / dx

    if n == 0:
        return f
    elif n == 1:
        return derivative
    else:
        return ordered_derivative(derivative, n-1)

# 4.4 #
# polar equation

def legendre(x, l, m):
    """ Associated Legendre Polynomial """
    f = lambda x: (x**2 - 1)**l
    df = ordered_derivative(f, l+m)
    return ((1-x**2)**(m/2))/(2**l * factorial(l)) * df(x)


def angular(theta, phi, l, m):
    """ Polar equation """

    # 1j is equivalent to i = sqrt(-1)
    PHI = np.exp(1j * m * phi)

    norm = (-1)**m * ( (2*l + 1)/(4 * pi) * (factorial(l - abs(m)) / factorial(l + abs(m))) )**0.5

    return norm * PHI * legendre(np.cos(theta), l, abs(m))


# 4.5 #
# radial equation

def laguerre(x, a, k):
    """ Associated Laguerre Polynomial """
    f = lambda x: np.exp(-x) * x**(k + a)
    df = ordered_derivative(f, k)
    return (x**(-a) * np.exp(-x)) / factorial(k) * df(x)

def radial(r, n, l):
    """ Radial equation """
    # common term - u
    u = (2 * r) / (n * a0)
    norm = (u**3 * ( factorial(n-l-1) / (2*n * (factorial(n+l))**3) ))**0.5
    return norm * np.exp(u/2) * (u**l) * laguerre(u, 2*l + 1, n-l-1)


# 4.6 #

# overall

def Psi(r, theta, phi, n, l, m):
    return radial(r, n, l) * angular(theta, phi, l, m)



def validate_quantum_numbers(n, l, m):
    """ Ensure quantum numbers are within range. """

    assert isinstance(n, int), "n ({}) is not an integer".format(n)
    assert isinstance(l, int), "l ({}) is not an integer".format(l)
    assert isinstance(m, int), "m ({}) is not an integer".format(m)

    assert n >= 1, "n ({}) must be greater than 1".format(n)
    assert 0 <= l <= n-1, "1 <= l <= n-1, l: {} failed".format(l)
    assert -l <= m <= l, "-l <= m <= l, m: {} failed".format(m)

def graph(n, l, m, resolution=1000):
    
    # parameters for the plot (tuned such that the bohr radius is on the same scale as # pixels
    frame_apothem = 500

	# create array of data points
    x = np.linspace(-frame_apothem*1.6,frame_apothem*1.6,int(resolution*1.6))
    y = np.linspace(-frame_apothem,frame_apothem,resolution)

    # square
    X, Y = np.meshgrid(x, x)

    r = np.sqrt(X**2 + Y**2)
    theta = np.arctan(X/Y+1e-10)
    phi = 0

	# create an array of wavefunction values (1e-10 added so that arctan never sees X/0)
    Z = np.abs(Psi(r, theta, phi, n, l, m))**2

    Z = Z.astype(np.float)
    Z = np.sqrt(Z)
    # this is done to "raise" the lower, less perceptible values to sight
    # plot the wavefunction in grayscale

    plt.subplot(2, 1, 1)
    plt.imshow(Z, cmap=cm.Greys_r)

    theta = pi
    phi = np.arctan(X/Y+1e-10)
    Z = np.abs(Psi(r, theta, phi, n, l, m))**2
    Z = Z.astype(np.float)
    Z = np.sqrt(Z)

    plt.subplot(2, 1, 2)
    plt.imshow(Z, cmap=cm.Greys_r)

    # phi = -pi
    # Z = np.abs(Psi(r, theta, phi, n, l, m))**2
    # Z = Z.astype(np.float)
    # Z = np.sqrt(Z)

    # plt.subplot(3, 1, 3)
    # plt.imshow(Z, cmap=cm.Greys_r)

    plt.show(block=False)


###

if __name__ == "__main__":
    
    n = 1
    l = 0
    m = 0

    validate_quantum_numbers(n, l, m)

    graph(n, l, m)

    # f = lambda x: x^3
    # print(ordered_derivative(f, ))