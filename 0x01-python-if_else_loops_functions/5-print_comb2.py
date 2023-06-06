#!/usr/bin/python3
for i in range(ord('0'),ord('9')+1):
    for j in range(ord('0'),ord('9')+1):
        if i != ord('9') or j != ord('9'):
            print("{}{}".format(chr(i),chr(j)), end = ', ')
        else:
            print("{}{}".format(chr(i),chr(j)))
