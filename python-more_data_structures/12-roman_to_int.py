#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    #  start off with making a dictionary
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    #  prev is the last letter we checked so we manage IV and IX etc
    total = 0
    prev = 0
    #  read roman numerals backwards and this makes WAY more sense
    for char in reversed(roman_string):
        value = values.get(char, 0)
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total
