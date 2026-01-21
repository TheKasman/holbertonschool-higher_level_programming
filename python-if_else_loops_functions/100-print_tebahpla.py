#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    c = chr(i)
    if (ord('z') - i) % 2 == 1:
        c = c.upper()
    print("{}".format(c), end="")
