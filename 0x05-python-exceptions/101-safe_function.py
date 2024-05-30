#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as erro:
        result = None
        print("Exception: {}".format(erro), file=stderr)
        return result
