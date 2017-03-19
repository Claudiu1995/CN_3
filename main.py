from get_matrix import read_matrix
from sum_matrix import sum_matrices


def main():
    matrix_A = read_matrix("a.txt", 10)
    matrix_B = read_matrix("b.txt", 10)
    matrix_A_plus_B = read_matrix("aplusb.txt", 20)

    print(matrix_A_plus_B == sum_matrices(matrix_A, matrix_B))


main()
