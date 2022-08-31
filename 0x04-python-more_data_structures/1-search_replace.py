#!/usr/bin/python3

def search_replace(my_list, search, replace):
    search_list = my_list[:]
    for i in range(len(search_list)):
        if search_list[i] == search:
            search_list[i] = replace
    return (search_list)
