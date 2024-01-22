#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if not size:
        return (None)
    else:
        i = 0
        for n in my_list:
            if n > i:
                i = n
    return (n)
