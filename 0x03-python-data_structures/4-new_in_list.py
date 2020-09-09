#!/usr/bin/python3
def new_in_list(my_list, i, e):
    if i < 0:
        return my_list
    if i > len(my_list) - 1:
        return my_list
    new = my_list[:]
    new[i] = e
    return new
