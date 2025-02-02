# L6 - Linear Interpolation
def linear_interpolation(table_points, x):
    for i in range(len(table_points) - 1):
        x1, y1 = table_points[i]
        x2, y2 = table_points[i + 1]
        if x1 <= x <= x2:
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            return y

    if x < table_points[0][0]:
        x1, y1 = table_points[0]
        x2, y2 = table_points[1]
    else:
        x1, y1 = table_points[-2]
        x2, y2 = table_points[-1]
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return y


def main():
    table_points = [(0.2, 13.7251), (0.35, 13.9776), (0.45, 14.0625), (0.6, 13.9776),
                    (0.75, 13.7241), (0.85, 13.3056), (0.9, 12.7281)]

    x = 0.65

    print("\nTable Points:", table_points)
    print("\nFinding an approximation of the value:", x)

    y = linear_interpolation(table_points, x)

    print(f"The approximation of the value {x} is: {round(y, 4)}")


if __name__ == "__main__":
    main()