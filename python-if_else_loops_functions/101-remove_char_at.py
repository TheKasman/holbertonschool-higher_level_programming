#!/usr/bin/python3
def remove_char_at(str, n):
    copystring = ""
    for i in range(len(str)):
        if i != n:
            copyString += str[i]
    return copyString
