#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        i = 0
        for n in my_list:
            if n > i:
                i = n
    return (n)
