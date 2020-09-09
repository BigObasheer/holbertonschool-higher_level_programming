#!/usr/bin/python3
def replace_in_list(my_list, i, e):
    if i < 0:
        return(my_list)

    element = len(my_list) - 1
    if i < element:
        return(my_list)

    else:
        my_list[i] = e
        return(my_list)
