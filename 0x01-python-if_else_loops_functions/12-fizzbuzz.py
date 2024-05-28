#!/usr/bin/python3
for i in range(101):
    if i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    elif i % 5 == 0 and i % 3 == 0:
        i = "FizzBuzz"
    print("{}".format(i), end=" ")