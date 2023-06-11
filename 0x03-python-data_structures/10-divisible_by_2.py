#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    newList = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            newList[i] = 1
        else:
            newList[i] = 0
    return newList
