# L6 - Lagrange Interpolation

def lagrange_interpolation(table_points, x):
    result = 0
    for i in range(len(table_points)):
        xi, yi = table_points[i]
        li = 1
        for j in range(len(table_points)):
            if i != j:
                xj, _ = table_points[j]
                li *= (x - xj) / (xi - xj)
        result += li * yi
    return result


def main():
    table_points = [(0.2, 13.7251), (0.35, 13.9776), (0.45, 14.0625), (0.6, 13.9776), (0.75, 13.7241), (0.85, 13.3056), (0.9, 12.7281)]
    x = 0.65

    print("\nTable Points:", table_points)
    print("\nFinding an approximation of the value:", x)

    y = lagrange_interpolation(table_points, x)

    print(f"The approximation of the value {x} is: {round(y, 4)}")


if __name__ == "__main__":
    main()