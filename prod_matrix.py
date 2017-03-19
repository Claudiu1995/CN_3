def get_val_line_pairs_from(matrix: tuple, column: int) -> list:
    diagonal = matrix[0]
    vector = matrix[1]

    val_line_pairs = []
    last_line = 0
    for i in range(0, len(vector)):
        if vector[i][1] < 0:
            last_line = -vector[i][1]
        elif vector[i][1] == column:
            val_line_pairs.append((vector[i][0], last_line))

    diagonal_value = diagonal[column - 1]
    diagonal_val_line_pair = (diagonal_value, column)
    val_line_pairs = insert_diagonal_value_into(val_line_pairs,
                                                diagonal_val_line_pair)
    return val_line_pairs


def insert_diagonal_value_into(val_col_pairs: list,
                               diagonal_val_col_pair: tuple) -> list:
    i = len(val_col_pairs)
    while i > 0 and val_col_pairs[i - 1][1] > diagonal_val_col_pair[1]:
        i -= 1
    val_col_pairs.insert(i, diagonal_val_col_pair)
    return val_col_pairs


def get_multiply_result_of(val_col_pairs: list, val_line_pairs: list) -> float:
    i = 0
    j = 0
    n = len(val_col_pairs)
    m = len(val_line_pairs)

    result = 0

    while i < n and j < m:
        col = val_col_pairs[i][1]
        line = val_line_pairs[j][1]
        if line == col:
            result = result + val_col_pairs[i][0] * val_line_pairs[j][0]
            i += 1
            j += 1
        elif line < col:
            j += 1
        else:
            i += 1

    return result


def multiply_matrices(matrix_A: tuple, matrix_B: tuple,
                      no_of_columns_B: int) -> tuple:
    diagonal_of_A = matrix_A[0]
    vector_of_A = matrix_A[1]

    diagonal_of_prod = []
    vector_of_prod = []

    val_col_pairs = []
    current_line = 1
    vector_of_prod.append(vector_of_A[0])

    for i in range(1, len(vector_of_A)):
        col = vector_of_A[i][1]
        if col < 0:
            diagonal_value = diagonal_of_A[current_line - 1]
            diagonal_val_col_pair = (diagonal_value, current_line)
            val_col_pairs = insert_diagonal_value_into(val_col_pairs,
                                                       diagonal_val_col_pair)
            for j in range(1, no_of_columns_B + 1):
                val_line_pairs = get_val_line_pairs_from(matrix_B, j)
                result = get_multiply_result_of(val_col_pairs, val_line_pairs)
                print(current_line, j)
                if current_line == j:
                    diagonal_of_prod.append(result)
                elif result > 0:
                    vector_of_prod.append((result, j))
            val_col_pairs = []
            current_line = -col
            vector_of_prod.append(vector_of_A[i])
        else:
            val_col_pairs.append(vector_of_A[i])

    return diagonal_of_prod, vector_of_prod
