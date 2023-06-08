#!/usr/bin/python3
from sys import argv
sum = 0
for s in argv[1:]:
    sum += int(s)
print("{:d}".format(sum))
