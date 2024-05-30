#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divr = a / b
        return divr
    except ZeroDivisionError:
        divr = None
        return divr
    finally:
        print("Inside result: {}".format(divr))
