#!/usr/bin/python3
i = 90
while i <= 90 and i >= 65:
    if i % 2 != 0:
        char = chr(i)
    else:
        char = chr(i + 32)
    print("{}".format(char), end="")
    i -= 1
