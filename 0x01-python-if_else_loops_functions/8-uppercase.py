#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print('{}'.format(
                chr(ord(str[i]) - ((ord('a')-ord('A'))))), end='')
        else:
            print('{}'.format(chr(ord(str[i]))), end='')
