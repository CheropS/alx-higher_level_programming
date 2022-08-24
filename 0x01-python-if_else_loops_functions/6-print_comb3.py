#!/usr/bin/python3

"""program that prints all possible different combinations of two digit"""

for a in range(0, 10):
        for b in range(a +1, 10):

            if a == 5 and b ==6:
                print(f"{a}{b}")
            else:
                print("{}{}".format(a, b), end=", ")
