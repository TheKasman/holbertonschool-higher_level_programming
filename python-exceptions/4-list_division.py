#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    answer = []
    try:
        for i in range(list_length):
            try:
                answer.append(my_list_1[i] / my_list_2[i])
            except IndexError:
                print("out of range")
                answer.append(0)
            except TypeError:
                print("wrong type")
                answer.append(0)
            except ZeroDivisionError:
                print("division by 0")
                answer.append(0)
    finally:
        return answer
