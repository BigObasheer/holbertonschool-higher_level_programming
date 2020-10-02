#!/usr/bin/python3
""" Python Test Development """


def matrix_divided(matrix, div):
    """
    Matrix Divided
    """

    matrixerror = "matrix must be a matrix (list of lists) of integers/floats"
    emptyargs = "matrix_divided() missing 2 required positional arguments\
: 'matrix' and 'div'"

    if matrix is None and div is None:
        raise TypeError(emptyargs)
    if matrix is None or type(matrix) is not list:
        raise TypeError(matrixerror)

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div is None or div == 0:
        raise ZeroDivisionError("division by zero")

    listcount = len(matrix)

    if listcount < 1:
        raise TypeError(matrixerror)

    elementcount = 0
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(matrixerror)
        for elements in lists:
            if type(elements) not in [float, int]:
                raise TypeError(matrixerror)
            elementcount += 1

    if elementcount % listcount != 0:
        raise TypeError("Each row of the matrix must have the same size")

    div_mat = []
    div = int(div)
    for nums in matrix:
        div_mat.append(list(map(lambda nums: round(nums / div, 2), nums)))

    return div_mat
