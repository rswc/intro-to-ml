import numpy as np

def pillar(X):
    Y = np.zeros_like(X)
    Y[np.abs(X - 0.5) < 0.2] = 1

    return Y

def three_levels(X):
    Y = pillar(X)

    Y[X > 0.7] = 0.3

    return Y

def triangle(X):
    return 1 - 2 * np.abs(X - 0.5)

def sine(X):
    return np.sin(X * 3.14)

def sin_over_x(X):
    Y = 20 * X

    return np.sin(Y)
