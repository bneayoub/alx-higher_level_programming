#!/usr/bin/python3
def element_at(mylist, idx):
    if idx < 0 or idx >= len(mylist):
        return None
    else:
        return mylist[idx]
