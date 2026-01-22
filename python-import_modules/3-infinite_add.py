#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    for i in range(1, len(sys.argv[i])):
        result = int(sys.argv[i]) + int(sys.argv[i + 1])
        print("{}".format(result))
