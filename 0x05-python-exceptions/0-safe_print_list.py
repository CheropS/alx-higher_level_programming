#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    ptr = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j], end="")
            ptr += 1
        except IndexError:
            break
    print("")
    return (ptr)
