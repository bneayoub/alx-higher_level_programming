#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    newstr = str[0:n]
    newstr += str[n+1:]
    return newstr
