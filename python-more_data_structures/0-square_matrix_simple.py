#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for row in matrix:
        matrix_2.append(list(map(lambda x: x ** 2, row)))
    return matrix_2
