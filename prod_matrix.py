def get_val_line_pairs_from(matrix: tuple, column: int) -> list:
    diagonal = matrix[0]
    vector = matrix[1]

    diagonal_value = diagonal[column - 1]
    diagonal_val_line_pair = (diagonal_value, column)
    insert_diagonal = True

    val_line_pairs = []
    last_line = 0
    for i in range(0, len(vector)):
        if vector[i][1] < 0:
            last_line = -vector[i][1]
        elif vector[i][1] == column:
            if last_line > column and insert_diagonal:
                insert_diagonal = False
                val_line_pairs.append(diagonal_val_line_pair)
            val_line_pairs.append((vector[i][0], last_line))

    if insert_diagonal:
        val_line_pairs.append(diagonal_val_line_pair)
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
    len_diagonal_of_A = len(diagonal_of_A)

    diagonal_of_prod = []
    vector_of_prod = []

    val_col_pairs = []
    current_line = 1
    vector_of_prod.append(vector_of_A[0])

    diagonal_value = diagonal_of_A[current_line - 1]
    diagonal_val_col_pair = (diagonal_value, current_line)
    insert_diagonal = True

    val_line_pairs_of_matrix_B = []
    for j in range(1, no_of_columns_B + 1):
        val_line_pairs_of_matrix_B.append(get_val_line_pairs_from(matrix_B, j))

    for i in range(1, len(vector_of_A)):
        col = vector_of_A[i][1]
        if col < 0:
            if insert_diagonal:
                val_col_pairs.append(diagonal_val_col_pair)

            for j in range(0, len(val_line_pairs_of_matrix_B)):
                val_line_pairs = val_line_pairs_of_matrix_B[j]
                result = get_multiply_result_of(val_col_pairs, val_line_pairs)
                if current_line == j + 1:
                    diagonal_of_prod.append(result)
                elif result > 0:
                    vector_of_prod.append((result, j))

            val_col_pairs = []
            current_line = -col
            vector_of_prod.append(vector_of_A[i])

            if current_line <= len_diagonal_of_A:
                diagonal_value = diagonal_of_A[current_line - 1]
                diagonal_val_col_pair = (diagonal_value, current_line)
                insert_diagonal = True
        else:
            if col > current_line and insert_diagonal:
                insert_diagonal = False
                val_col_pairs.append(diagonal_val_col_pair)
            val_col_pairs.append(vector_of_A[i])

    return diagonal_of_prod, vector_of_prod
