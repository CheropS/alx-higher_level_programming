#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ptr = 0

    try:
        for i in my_list:
            if ptr < x:
                print('{}'.format(my_list[ptr]), end='')
                ptr += 1

        print()
    except TypeError:
        pass
    finally:
        return ptr
