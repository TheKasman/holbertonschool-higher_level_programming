#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """N is our triangle size."""
    triangle = []

    for row_n in range(n):
        row = []
        for i in range(row_n + 1):
            if i == 0 or i == row_n:
                current_value = 1
            else:
                current_value = triangle[row_n - 1][i - 1]
                + triangle[row_n - 1][i]

            row.append(current_value)
        triangle.append(row)
        print(row)
