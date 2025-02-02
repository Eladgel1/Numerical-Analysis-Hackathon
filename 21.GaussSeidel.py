# L4 - Gauss Seidel
import numpy as np


def swap_row(mat, row1, row2):
    mat[[row1, row2]] = mat[[row2, row1]]


def gaussianElimination(A, b):
    N = len(A)
    AugmentedMatrix = np.hstack((A, b.reshape(-1, 1)))

    print("\nInitial Augmented Matrix:")
    print_matrix(AugmentedMatrix)

    singular_flag = forward_substitution(AugmentedMatrix)

    if singular_flag != -1:
        if AugmentedMatrix[singular_flag, -1] != 0:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    return backward_substitution(AugmentedMatrix)


def forward_substitution(mat):
    N = len(mat)
    for k in range(N):
        max_row = max(range(k, N), key=lambda i: abs(mat[i, k]))
        if mat[max_row, k] == 0:
            return k

        if max_row != k:
            swap_row(mat, k, max_row)

        print(f"\nMatrix after swapping row {k} with row {max_row}:")
        print_matrix(mat)

        for i in range(k + 1, N):
            factor = mat[i, k] / mat[k, k]
            mat[i, k:] -= factor * mat[k, k:]

        print(f"\nMatrix after elimination in column {k}:")
        print_matrix(mat)

    return -1


def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)

    for i in range(N - 1, -1, -1):
        if mat[i, i] == 0:
            raise ValueError("Division by zero detected during back substitution.")

        x[i] = (mat[i, -1] - np.dot(mat[i, i + 1:N], x[i + 1:N])) / mat[i, i]

    return x


def print_matrix(mat):
    for row in mat:
        print(" ".join(f"{elem:10.6f}" for elem in row))


A = np.array([
    [1, 0.5, 1 / 3],
    [0.5, 1 / 3, 0.25],
    [1 / 3, 0.25, 0.2]
])

b = np.array([1, 0, 0])

solution = gaussianElimination(A, b)

if isinstance(solution, str):
    print(solution)
else:
    print("\nSolution for the system (a, b, c):")
    for i, val in enumerate(solution):
        print(f"x{i + 1} = {val:.6f}")
