#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_ch = None
    if sentence:
        first_ch = sentence[0]
    return (length, first_ch)
