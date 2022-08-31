#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(h, a_dictionary[h])) for h in sorted(a_dictionary)]
