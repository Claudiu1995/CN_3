from math import *

epsilon = pow(10, -8)


def equals(matrix_A: tuple, matrix_B: tuple) -> bool:
    diagonal_of_A = matrix_A[0]
    vector_of_A = matrix_A[1]
    diagonal_of_B = matrix_B[0]
    vector_of_B = matrix_B[1]

    if abs(len(diagonal_of_A) - len(diagonal_of_B)) >= epsilon:
        print("diag dim", len(diagonal_of_A), len(diagonal_of_B))
        return False

    for i in range(0, len(diagonal_of_A)):
        if abs(diagonal_of_A[i] - diagonal_of_B[i]) >= epsilon:
            print("diag", diagonal_of_A[i], diagonal_of_B[i])
            return False

    if abs(len(vector_of_A) - len(vector_of_B)) >= epsilon:
        print("vect dim", len(vector_of_A), len(vector_of_B))
        return False

    for i in range(0, len(vector_of_A)):
        val_A = vector_of_A[i][0]
        val_B = vector_of_B[i][0]

        if abs(val_A - val_B) >= epsilon:
            print("val", val_A, val_B)
            return False

    return True
