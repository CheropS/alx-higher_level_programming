#!/usr/bin/python3

"""prints numbers from 0 to 99 in a list format separated by ,"""

for number in range(0,100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")