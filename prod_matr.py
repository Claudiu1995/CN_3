def get_val_col_pairs_from(matrix: tuple, line: int) -> list:
    diagonal = matrix[0]
    vector = matrix[1]

    for i in range(0, len(vector)):
        if vector[i][1] == -line:
            first_index = i
        if vector[i][1] == -line - 1:
            second_index = i
            return vector[first_index + 1:second_index]


def get_val_line_pairs_from(matrix: tuple, column: int) -> list:
    diagonal = matrix[0]
    vector = matrix[1]

    val_col_pairs = []
    last_line = 0
    for i in range(0, len(vector)):
        if vector[i][1] < 0:
            last_line = -vector[i][1]
        elif vector[i][1] == column:
            val_col_pairs.append((vector[i][0], last_line))
        elif last_line == column:
            val_col_pairs.append((diagonal[last_line - 1], last_line))
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


def prod_matr(matrix_A, matrix_B, no_of_lines_A, no_of_columns_B):
    diagonal_of_A = matrix_A[0]
    vector_of_A = matrix_A[1]
    diagonal_of_B = matrix_B[0]
    vector_of_B = matrix_B[1]

    diagonal_of_prod = []
    vector_of_prod = []

    for i in range(0, no_of_lines_A):
        vector_of_prod.append((0, -(i + 1)))
        val_col_pairs = get_val_col_pairs_from(i, vector_of_A)
        for j in range(0, no_of_columns_B):
            val_line_pairs = get_val_line_pairs_from(vector_of_B, j)
            result = get_multiply_result_of(val_col_pairs, val_line_pairs)
