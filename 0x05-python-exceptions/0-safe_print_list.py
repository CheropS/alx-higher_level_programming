#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.
    Args:
        my_list (list): original list.
        x (int): number of elements to print.
    Returns:
        Number of elements to be printed.
    """
    ret = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j], end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
