#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value.isdigit():
            print("{}".format(value))
            return True
    except ValueError:
        print("{} is not an integer".format(value))
    


value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))