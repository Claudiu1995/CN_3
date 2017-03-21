def read_matrix(file_name: str, nr_of_non_null_val_per_line: int) -> tuple:
    with open(file_name) as fd:
        n = [int(x) for x in next(fd).split()][0]
        next(fd)
        b = []
        for i in range(0, n):
            b.append([float(x) for x in next(fd).split()][0])
        next(fd)
        dictionar = {}
        for line in fd:
            if len(line) <= 1:
                continue
            split_line = line.split(", ")
            x = float(split_line[0])
            i = int(split_line[1])
            j = int(split_line[2])
            if i in dictionar:
                if j in dictionar[i]:
                    dictionar[i][j] += x
                else:
                    dictionar[i][j] = x
            else:
                dictionar[i] = {}
                dictionar[i][j] = x
                if len(dictionar[i]) > nr_of_non_null_val_per_line:
                    raise Exception("For matrix from file {0} the line {1} has"
                                    " too much non null elements!"
                                    .format(file_name, i))

    d_b, val_col_b = convert_column_vector_to_matrix(b)

    d_A = []
    val_col_A = []
    for i in range(0, n):
        d_A.append(dictionar[i][i])
        val_col_A.append((0, -(i + 1)))
        for j in range(0, n):
            if i == j or j not in dictionar[i]:
                continue
            val_col_A.append((dictionar[i][j], j + 1))
    val_col_A.append((0, -(n + 1)))

    return (d_A, val_col_A), (d_b, val_col_b)


def convert_column_vector_to_matrix(array: list):
    n = len(array)
    d_b = [array[0]]
    val_col_b = [(0, -1)]
    for i in range(1, n):
        val_col_b.append((0, -(i + 1)))
        val_col_b.append((array[i], 1))
    val_col_b.append((0, -(n + 1)))
    return d_b, val_col_b
