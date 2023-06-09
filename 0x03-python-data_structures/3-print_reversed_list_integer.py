#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        print("{}".format(my_list[len(my_list) - i - 1]))
