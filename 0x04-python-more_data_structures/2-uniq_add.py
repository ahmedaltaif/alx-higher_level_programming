#!/usr/bin/python3
def uniq_add(my_list=[]):
    ne_list = list(set(my_list))
    result = 0
    for i in ne_list:
        result += i
    return result
