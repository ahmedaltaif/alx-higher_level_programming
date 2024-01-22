#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lis_a = list(tuple_a)
    lis_b = list(tuple_b)
    while len(lis_a) < 2:
        lis_a.append(0)
    while len(lis_b) < 2:
        lis_b.append(0)
    resl = [lis_a[0] + lis_b[0], lis_a[1] + lis_b[1]]
    return(tuple(resl))
