#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    oper = sys.argv[2]
    b = int(sys.argv[3])

    if oper == "+":
        result = add(a, b)
    elif oper == "-":
        result = sub(a, b)
    elif oper == "*":
        result = mul(a, b)
    elif oper == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, oper, b, result))
