#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
        else:
            return False
    except ValueError:
        print("{} is not an integer".format(value))
