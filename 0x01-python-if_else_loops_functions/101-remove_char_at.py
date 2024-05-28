#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for i in str:
        if str.index(i) == n:
            continue
        else:
            newstr += i  
    return newstr
    