#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    total = sum(score * weight for score, weight in my_list)
    weights = sum(weight for x, weight in my_list)

    return total / weights
