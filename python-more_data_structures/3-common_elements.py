#!/usr/bin/python3
def common_elements(set_1, set_2):
    match = []
    for x in set_1:
        if x in set_2:
            match.append(x)
    return match
