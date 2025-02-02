import numpy as np


def romberg_integration(func, a, b, n):
    h = b - a
    R = np.zeros((n, n), dtype=float)

    R[0, 0] = 0.5 * h * (func(a) + func(b))
    print(f"R[0,0] = {R[0,0]:.9f}")

    for i in range(1, n):
        h /= 2
        sum_term = 0

        for k in range(1, 2 ** i, 2):
            sum_term += func(a + k * h)

        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_term
        print(f"R[{i},0] = {R[i,0]:.9f}")

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4 ** j) - 1)
            print(f"R[{i},{j}] = {R[i,j]:.9f}")

    return R[n - 1, n - 1]


def f(x):
    return np.sin(2 * np.exp(-2*x)) / ((2*x**3 + 5*x**2 - 6))


if __name__ == '__main__':
    a = -0.5
    b = 0.5
    n = 5
    integral = romberg_integration(f, a, b, n)

    print(f"\nDivision into n={n} sections")
    print(f"Approximate integral in range [{a},{b}] is {integral:.9f}")