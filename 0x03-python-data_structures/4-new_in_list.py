#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = []
    for e in my_list:
        newList.append(e)

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        newList[idx] = element
        return newList
