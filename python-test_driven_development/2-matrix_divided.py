#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Check if matrix is valid
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows are of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is valid
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(elem/div, 2) for elem in row] for row in matrix]

    return new_matrix
