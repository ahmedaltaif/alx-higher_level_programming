#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divr = a / b
        return divr
    except (TypeError, ZeroDivisionError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(divr))

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
