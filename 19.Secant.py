# L2 - Secant Method
import numpy as np


def f(x):
    return x * np.exp(-x ** 2 + 5 * x) * (2 * x ** 2 - 3 * x - 5)


def secant_method(f, x0, x1, TOL, N=50):
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "x0", "x1", "p"))
    for i in range(N):
        if f(x1) - f(x0) == 0:
            print("Method cannot continue.")
            return None

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(p - x1) < TOL:
            return p
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1, p))
        x0 = x1
        x1 = p

    return p


x0, x1 = 2.6, 3
TOL = 1e-6
N = 50

root = secant_method(f, x0, x1, TOL, N)
print(f"\n The equation f(x) has an approximate root at x = {root}")
