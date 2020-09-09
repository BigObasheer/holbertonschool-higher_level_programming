#!/usr/bin/python3
def element_at(my_list, i):
    if i < 0:
        return None

    elementcount = len(my_list) - 1

    if i > elementcount:
        return None

    return my_list[i]
