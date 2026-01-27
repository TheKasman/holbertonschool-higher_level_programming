#!/usr/bin/python3
def no_c(my_string):
    fixed = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue  # skip the letter
        fixed += i
    return fixed
