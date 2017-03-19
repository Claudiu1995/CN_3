import sys
from get_storing import get_d_val_col


def main():
    d, val_col = get_d_val_col("test.txt")
    print(d)
    print(val_col)


main()
