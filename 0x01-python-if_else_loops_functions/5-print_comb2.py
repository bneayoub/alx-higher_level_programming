#!/usr/bin/python3
for i in range(100):
    code = "{:02d}".format(i)
    if i != 99:
        print(code, end=', ')
    else:
        print(code)
