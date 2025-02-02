# L4 - LU
import numpy as np


def decomposition_LU(matrix):
    n = len(matrix)
    A = np.array(matrix, dtype=float)

    L = np.zeros((n, n))
    U = np.zeros((n, n))

    print("\nLU Decomposition Steps:")
    for i in range(n):
        for k in range(i, n):
            sum_value = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_value

        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                sum_value = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_value) / U[i][i]

        print(f"Step {i + 1}: L =")
        print_mat(L.tolist())
        print(f"Step {i + 1}: U =")
        print_mat(U.tolist())
    return L, U


def solve_LU(L, U, b):
    n = L.shape[0]
    c = np.zeros(n)

    print("\nForward Substitution Steps:")
    for i in range(n):
        c[i] = b[i] - sum(L[i][k] * c[k] for k in range(i))
        c[i] = c[i] / L[i][i]
        print(f"c[{i}] = {c[i]:.9f}")

    x = np.zeros(n)
    print("\nBackward Substitution Steps:")
    for i in range(n - 1, -1, -1):
        x[i] = c[i] - sum(U[i][k] * x[k] for k in range(i + 1, n))
        x[i] = x[i] / U[i][i]
        print(f"x[{i}] = {x[i]:.9f}")

    return x.tolist()


def print_mat(matrix):
    for row in matrix:
        print("[" + " ".join(f"{elem:.9f}" for elem in row) + "]")


def main():
    A = np.array([
        [1, 0.5, 1 / 3],
        [0.5, 1 / 3, 0.25],
        [1 / 3, 0.25, 0.2]
    ])
    print("Matrix A:")
    print_mat(A.tolist())

    L, U = decomposition_LU(A)
    print("\nMatrix L:")
    print_mat(L.tolist())

    print("\nMatrix U:")
    print_mat(U.tolist())

    b = np.array([1, 0, 0])
    x = solve_LU(L, U, b)
    print("\nSolution vector x:")
    print(f"{x}")


if __name__ == "__main__":
    main()