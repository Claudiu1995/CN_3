def read_matrix(file_name: str, nr_of_non_null_val_per_line: int) -> tuple:
    with open(file_name) as fd:
        n = [int(x) for x in next(fd).split()][0]
        next(fd)
        b = [""]
        for i in range(0, n):
            b.append([float(x) for x in next(fd).split()][0])
        # print (b)
        next(fd)
        dictionar = {}
        for line in fd:
            if len(line) <= 1:
                continue
            # print(line)
            split_line = line.split(", ")
            # print split_line[0]
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

    d = []
    val_col = []
    for i in range(0, n):
        d.append(dictionar[i][i])
        val_col.append((0, -(i + 1)))
        for j in range(1, n + 1):
            if i == j or j not in dictionar[i]:
                continue
            val_col.append((dictionar[i][j], j))
    val_col.append((0, -(n + 1)))

    return d, val_col
