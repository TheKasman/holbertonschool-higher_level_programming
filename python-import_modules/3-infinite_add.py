#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    for i in range(1, len(sys.argv)):
        result = 0
        result += int(sys.argv[i])
        print("{}".format(result))
