#!/usr/bin/python3

def no_c(my_string):
    copy = [b for b in my_string if b != 'c' and b != 'C']
    return ("".join(copy))
