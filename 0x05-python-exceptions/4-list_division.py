#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    d = 0
    for i in my_list_1:
        for x in my_list_2:
            newList = []
            try:
                newList[d] = i / x
            except ValueError:
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
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