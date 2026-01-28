#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary

    keysToDelete = [key for key, val in a_dictionary.items() if val == value]

    for k in keysToDelete:
        del a_dictionary[k]

    return a_dictionary
