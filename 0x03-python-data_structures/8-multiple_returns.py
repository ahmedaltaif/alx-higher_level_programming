#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        size = len(sentence)
        return (size, sentence[0])
    else:
        return (0, None)
