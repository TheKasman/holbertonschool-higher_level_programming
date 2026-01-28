#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueList = []
    for x in my_list:
        if x not in uniqueList:
            uniqueList.append(x)
    return sum(uniqueList)
