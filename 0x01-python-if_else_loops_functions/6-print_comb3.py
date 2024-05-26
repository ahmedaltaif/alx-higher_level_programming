#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x + y != 17:
            if x != y and x < y:
                print("{}{},".format(x, y), end=" ")
        
print("{}".format("89", end=""))
        