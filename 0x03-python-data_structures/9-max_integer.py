#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if not size:
        return (None)
    else:
        max = my_list[0]
        for i in my_list[1:]:
            max = max if max >= i else i
        return max
