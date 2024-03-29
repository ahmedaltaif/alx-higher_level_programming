#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers"""
def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    listofi = list_of_integers
    lngth = len(listofi)
    if lngth == 0:
        return
    m = lngth // 2
    if (m == lngth - 1 or listofi[m] >= listofi[m + 1]) and (m == 0 or listofi[m] >= listofi[m - 1]):
        return listofi[m]
    if m != lngth - 1 and listofi[m + 1] > listofi[m]:
        return find_peak(listofi[m + 1:])
    return find_peak(listofi[:m])
