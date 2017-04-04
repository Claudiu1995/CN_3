from tkinter import *

from equal_matrix import equals
from get_matrix import *
from prod_matrix import multiply_matrices
from sum_matrix import sum_matrices
from time import time


def main():
    x = []
    for i in range(2017, -1, -1):
        x.append(i)
    vect_x = convert_column_vector_to_matrix(x)
    matrix_A, vect_A = read_matrix("a.txt", 10)
    matrix_B, vect_B = read_matrix("b.txt", 10)
    matrix_A_plus_B, vect_A_plus_B = read_matrix("aplusb.txt", 20)
    matrix_A_ori_B, vect_A_ori_b = read_matrix("aorib.txt", 100)

    msg_A_plus_B = "No"
    msg_A_ori_B = "No"
    msg_A_ori_x = "No"
    msg_B_ori_x = "No"
    msg_A_plus_B_ori_x = "No"
    msg_A_ori_B_ori_x = "No"

    sum_matrix = sum_matrices(matrix_A, matrix_B)
    print("16%")
    product_matrix = multiply_matrices(matrix_A, matrix_B)
    print("32%")
    product_matrix_vect_A = multiply_matrices(matrix_A, vect_x)
    print("48%")
    product_matrix_vect_B = multiply_matrices(matrix_B, vect_x)
    print("64%")
    product_matrix_vect_A_plus_B = multiply_matrices(matrix_A_plus_B, vect_x)
    print("80%")
    product_matrix_vect_A_ori_B = multiply_matrices(matrix_A_ori_B, vect_x)
    print("96%")

    if equals(matrix_A_plus_B, sum_matrix):
        msg_A_plus_B = "Yes"

    if equals(matrix_A_ori_B, product_matrix):
        msg_A_ori_B = "Yes"

    if equals(product_matrix_vect_A, vect_A):
        msg_A_ori_x = "Yes"

    if equals(product_matrix_vect_B, vect_B):
        msg_B_ori_x = "Yes"

    if equals(product_matrix_vect_A_plus_B, vect_A_plus_B):
        msg_A_plus_B_ori_x = "Yes"

    if equals(product_matrix_vect_A_ori_B, vect_A_ori_b):
        msg_A_ori_B_ori_x = "Yes"

    root = Tk()
    root.title("Tema 3")
    root.geometry("300x300")

    frame = Frame(root)
    frame.grid(sticky=E + W)

    Label(frame, text="Is sum of matrices correct?").grid(row=0, column=0, padx=3, pady=3)
    Label(frame, text=msg_A_plus_B).grid(row=0, column=1, padx=3, pady=3)
    Label(frame, text="Is product of matrices correct?").grid(row=1, column=0, padx=3,
                                                              pady=3)
    Label(frame, text=msg_A_ori_B).grid(row=1, column=1, padx=3, pady=3)
    Label(frame, text="Is A multiplied by x correct?").grid(row=2, column=0, padx=3,
                                                            pady=3)
    Label(frame, text=msg_A_ori_x).grid(row=2, column=1, padx=3, pady=3)
    Label(frame, text="Is B multiplied by x correct?").grid(row=3, column=0, padx=3,
                                                            pady=3)
    Label(frame, text=msg_B_ori_x).grid(row=3, column=1, padx=3, pady=3)
    Label(frame, text="Is A_plus_B multiplied by x correct?").grid(row=4, column=0,
                                                                   padx=3, pady=3)
    Label(frame, text=msg_A_plus_B_ori_x).grid(row=4, column=1, padx=3, pady=3)
    Label(frame, text="Is A_ori_B multiplied by x correct?").grid(row=5, column=0, padx=3,
                                                                  pady=3)
    Label(frame, text=msg_A_ori_B_ori_x).grid(row=5, column=1, padx=3, pady=3)
    print("100%")

    root.mainloop()

    # mat_1, vect_1 = read_matrix("test.txt", 10)
    # mat_2, vect_2 = read_matrix("test.txt", 10)
    # print(multiply_matrices(mat_1, mat_2, 5))

main()
