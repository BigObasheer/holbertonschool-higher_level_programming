#!/usr/bin/python3
def add_tuple(a=(), b=()):
    if len(a) == 0:
        a = (0, 0)
    if len(a) == 1:
        a = (a[0], 0)
    if len(b) == 0:
        b = (0, 0)
    if len(b) == 1:
        b = (b[0], 0)

    new = (a[0] + b[0], a[1] + b[1])
    return new
