from get_matrix import read_matrix
from sum_matrix import sum_matrices
from prod_matrix import multiply_matrices
import time


def main():
    matrix_A, vect_A = read_matrix("a.txt", 10)
    matrix_B, vect_B = read_matrix("b.txt", 10)
    matrix_A_plus_B, vect_A_plus_B = read_matrix("aplusb.txt", 20)
    matrix_A_ori_B, vect_A_ori_b = read_matrix("aorib.txt", 100)

    t = time.time()
    print(t)
    print(matrix_A_plus_B == sum_matrices(matrix_A, matrix_B))
    print(time.time()-t)
    #print(matrix_A_ori_B == multiply_matrices(matrix_A, matrix_B, 2017))
    # mat_1, vect_1 = read_matrix("test.txt", 10)
    # mat_2, vect_2 = read_matrix("test.txt", 10)
    # print(multiply_matrices(mat_1, mat_2, 5))

main()
