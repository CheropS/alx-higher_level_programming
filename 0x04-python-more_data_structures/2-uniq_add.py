#!/usr/bin/python3

def uniq_add(my_list=[]):
    answer = 0
    for f in set(my_list):
        answer += f
    return (answer)
