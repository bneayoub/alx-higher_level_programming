#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for line in matrix:
        for i in range(0, len(line)):
            if i != len(line) - 1:
                print("{:d}".format(line[i]), end=" ")
            else:
                print("{:d}".format(line[i]), end="\n")
