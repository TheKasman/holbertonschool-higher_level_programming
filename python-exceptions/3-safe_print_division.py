#!/usr/bin/python3
def safe_print_division(a, b):
    answer = 0
    try:
        answer = a / b
    except ZeroDivisionError:
        answer = None
        return None
    finally:
        print("Inside result: {}".format(answer))
    return answer
