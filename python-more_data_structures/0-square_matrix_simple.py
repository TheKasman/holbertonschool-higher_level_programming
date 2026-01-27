#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        newMatrix.append(new_row)
    return newMatrix
