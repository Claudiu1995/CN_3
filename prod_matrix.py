def get_val_line_pairs_list_of(matrix: tuple) -> list:
    diagonal = matrix[0]
    vector = matrix[1]
    diagonal_length = len(diagonal)

    val_line_pairs_list = [[] for i in range(0, diagonal_length)]
    current_line = 0
    for i in range(0, len(vector)):
        column = vector[i][1]
        if column < 0:
            current_line = -vector[i][1]
            index = current_line - 1
            if current_line <= diagonal_length:
                val_line_pairs_list[index].append((diagonal[index], current_line))
        else:
            index = column - 1
            val_line_pairs_list[index].append((vector[i][0], current_line))

    return val_line_pairs_list


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


def multiply_matrices(matrix_A: tuple, matrix_B: tuple) -> tuple:
    diagonal_of_A = matrix_A[0]
    vector_of_A = matrix_A[1]

    val_col_pairs = []
    diagonal_of_prod = []
    vector_of_prod = [vector_of_A[0]]

    current_line = 1
    use_diagonal_value = True

    val_line_pairs_list_of_matrix_B = get_val_line_pairs_list_of(matrix_B)

    for i in range(1, len(vector_of_A)):
        column = vector_of_A[i][1]
        if column < 0:
            if use_diagonal_value:
                val_col_pairs.append((diagonal_of_A[current_line - 1], current_line))

            for j in range(0, len(val_line_pairs_list_of_matrix_B)):
                val_line_pairs = val_line_pairs_list_of_matrix_B[j]
                product_result = get_multiply_result_of(val_col_pairs, val_line_pairs)
                if current_line == j + 1:
                    diagonal_of_prod.append(product_result)
                elif product_result > 0:
                    vector_of_prod.append((product_result, j + 1))

            vector_of_prod.append(vector_of_A[i])

            current_line = -column
            use_diagonal_value = True
            val_col_pairs = []
        else:
            if column > current_line and use_diagonal_value:
                use_diagonal_value = False
                val_col_pairs.append((diagonal_of_A[current_line - 1], current_line))
            val_col_pairs.append(vector_of_A[i])

    return diagonal_of_prod, vector_of_prod
