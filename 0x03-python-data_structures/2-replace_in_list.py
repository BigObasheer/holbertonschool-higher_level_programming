#!/usr/bin/python3
def replace_in_list(my_list, i, e):
    if idx < 0:
        return(my_list)

    element = len(my_list) - 1
    if element < idx:
        return(my_list)

    else:
        my_list[i] = e
        return(my_list)
