#!/usr/bin/python3

def multiple_returns(sentence):
    len = len(sentence)
    if len == 0:
        result = (0, None)
        return result
    else:
        result = (len, sentence[0:1])
        return result
