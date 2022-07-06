#!/usr/bin/python3

# function that computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    new_matrix = []
    # loop through outer list
    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda x: x*x, matrix[i])))
    # return in the new_matrix
    return new_matrix
