# L3 - Simpson
import numpy as np


def f(x):
    return np.sin(2 * np.exp(-2 * x)) / ((2 * x ** 3 + 5 * x ** 2 - 6))


def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n
    integral = f(a) + f(b)

    print(f"{'i':<5} {'x_i':<15} {'f(x_i)':<20} {'Multiplier'}")
    print(f"{0:<5} {a:<15.6f} {f(a):<20.6f} {1}")

    for i in range(1, n):
        x_i = a + i * h
        multiplier = 2 if i % 2 == 0 else 4
        integral += multiplier * f(x_i)

        print(f"{i:<5} {x_i:<15.6f} {f(x_i):<20.6f} {multiplier}")

    print(f"{n:<5} {b:<15.6f} {f(b):<20.6f} {1}")

    integral *= h / 3
    return integral


a, b = -0.5, 0.5
n = 10

integral_value = simpsons_rule(f, a, b, n)

print(f"\nNumerical Integration of definite integral in range [{a},{b}] is {integral_value}")


