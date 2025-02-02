# L1 - Newton Raphson
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
    f = lambda x: np.cos(2 * x ** 3 + 5 * x ** 2 - 6) / (2 * np.exp(-2 * x))
    df = lambda x: (-np.sin(2 * x ** 3 + 5 * x ** 2 - 6) * (6 * x ** 2 + 10 * x) / (2 * np.exp(-2 * x))) + \
                   (2 * np.cos(2 * x ** 3 + 5 * x ** 2 - 6) * np.exp(-2 * x)) / (2 * np.exp(-2 * x))

    p0 = 1.5
    TOL = 1e-6
    N = 100

    root = newton_raphson(f, df, p0, TOL, N)
    if root is not None:
        print("\nThe equation f(x) has an approximate largest root at x = {:<15.9f}".format(root))