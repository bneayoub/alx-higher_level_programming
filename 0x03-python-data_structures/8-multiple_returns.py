#!/usr/bin/python3

def multiple_returns(sentence):
    len = len(sentence)
    if len == 0:
        resultult = (0, None)
        return resultult
    else:
        result = (len, sentence[0:1])
        return result
