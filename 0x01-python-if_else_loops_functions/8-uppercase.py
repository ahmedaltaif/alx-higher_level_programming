#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 90 <= ord(i) <= 122:
            add = 32
        else:
            add = 0
        print("{:s}".format(chr(ord(i) - add)), end="")

    print()
