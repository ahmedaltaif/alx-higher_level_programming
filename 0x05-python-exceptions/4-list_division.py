#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    d = 0
    newList = []
    while d < list_length:
            try:
                result = my_list_1[d] / my_list_2[d]
            except TypeError:
                result = 0
                print("wrong type")
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                newList += [result]
            d += 1
    return newList




my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)