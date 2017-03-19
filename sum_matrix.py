def get_values_from(val_list: list, index: int) -> tuple:
    val_col_pair = val_list[index]
    val = val_col_pair[0]
    col = val_col_pair[1]
    return val, col


def sum_matrices(matrix_A: tuple, matrix_B: tuple) -> tuple:
    diagonal_of_A = matrix_A[0]
    vector_of_A = matrix_A[1]
    diagonal_of_B = matrix_B[0]
    vector_of_B = matrix_B[1]
    diagonal_of_sum = []
    vector_of_sum = []

    n = len(diagonal_of_A)
    if n != len(diagonal_of_B):
        raise Exception("Can not sum square matrix with different rank.")

    for i in range(0, n):
        diagonal_of_sum.append(diagonal_of_A[i] + diagonal_of_B[i])

    current_line = 1
    i = 0
    j = 0

    val_A, col_A = get_values_from(vector_of_A, i)
    val_B, col_B = get_values_from(vector_of_B, j)

    while current_line < n + 1:
        if col_A < 0 and col_B < 0:
            if col_A == col_B:
                current_line = -col_A
                vector_of_sum.append((val_A, col_A))
                i += 1
                j += 1
                if current_line < n + 1:
                    val_A, col_A = get_values_from(vector_of_A, i)
                    val_B, col_B = get_values_from(vector_of_B, j)
            else:
                raise Exception("col_A and col_B are negative and not equal")

        while col_A > 0 and col_B > 0:
            if col_A < col_B:
                vector_of_sum.append((val_A, col_A))
                i += 1
                val_A, col_A = get_values_from(vector_of_A, i)
            elif col_B < col_A:
                vector_of_sum.append((val_B, col_B))
                j += 1
                val_B, col_B = get_values_from(vector_of_B, j)
            else:
                vector_of_sum.append((val_A + val_B, col_A))
                i += 1
                j += 1
                val_A, col_A = get_values_from(vector_of_A, i)
                val_B, col_B = get_values_from(vector_of_B, j)

        while col_A > 0:
            vector_of_sum.append((val_A, col_A))
            i += 1
            val_A, col_A = get_values_from(vector_of_A, i)

        while col_B > 0:
            vector_of_sum.append((val_B, col_B))
            j += 1
            val_B, col_B = get_values_from(vector_of_B, j)

    return diagonal_of_sum, vector_of_sum
