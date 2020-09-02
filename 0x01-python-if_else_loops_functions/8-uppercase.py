#!/usr/bin/python3
def uppercase(str):
    for i in str:
        upper = i
        if ord(i) >= 97 and ord(i) <= 122:
            upper = chr(ord(i) - 32)
        print("{}".format(upper), end="")
    print("")
