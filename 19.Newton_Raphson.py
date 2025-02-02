# L2 - Newton Raphson
import numpy as np


def newton_raphson(f, df, p0, TOL, N=50):
    print("{:<10} {:<15} {:<15}".format("Iteration", "p0", "p1"))
    for i in range(N):
        if df(p0) == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return None

        p = p0 - f(p0) / df(p0)

        print("{:<10} {:<15.9f} {:<15.9f}".format(i, p0, p))

        if abs(p - p0) < TOL:
            return p
        p0 = p
    return p


if __name__ == '__main__':
    f = lambda x: (x * np.exp(-x ** 2 + 5 * x)) * (2 * x ** 2 - 3 * x - 5)
    df = lambda x: (np.exp(-x ** 2 + 5 * x) * (2 * x ** 2 - 3 * x - 5)) + (
                x * np.exp(-x ** 2 + 5 * x) * (-2 * x + 5) * (2 * x ** 2 - 3 * x - 5)) + (
                               x * np.exp(-x ** 2 + 5 * x) * (4 * x - 3))

    p0 = 3
    TOL = 1e-6
    N = 100

    root = newton_raphson(f, df, p0, TOL, N)
    if root is not None:
        print("\nThe equation f(x) has an approximate largest root at x = {:<15.9f}".format(root))