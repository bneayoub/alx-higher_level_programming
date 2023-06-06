#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        string = chr(ord(str[i]))
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            string = chr(ord(str[i]) - ((ord('a')-ord('A'))))
        print('{}'.format(string), end='')
    print('\n', end='')
