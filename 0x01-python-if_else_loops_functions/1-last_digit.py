#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
print(dir(random))

digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("last digit of {} is {} and is " .format(number, digit), end="")

if digit > 5:
    print("and is greater than 5")
elif digit in range (1, 6):
    print("and is less than 6 and not 0")
else:
    print("and is 0")
