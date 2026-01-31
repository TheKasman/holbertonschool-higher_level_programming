#!/usr/bin/python3
"""
Divides all elements of a matrix by a number.

Args:
    matrix: A list of lists of numbers.
    div: The number to divide by.

Returns:
    A new matrix with each value divided by div.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix = [[1, 2, 3], [4]]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 'nan')
    Traceback (most recent call last):
    TypeError: div must be a number

    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Validate each element
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    # Validate row sizes
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Build new matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
