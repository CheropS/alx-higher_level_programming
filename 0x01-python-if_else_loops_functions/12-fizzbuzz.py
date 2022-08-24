#!/usr/bin/python3

"""prints fizzbuzz if it is not a multiple of 3 or 5\
        prints fizz for multiples of 3\
        prints buzz for mulltiples of 5."""

def fizzbuzz():
    for number in range(0,101):
        if number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
            print("Buzz", end="")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        else:
            print("{} ".format(number), end="")

