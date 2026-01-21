#!/usr/bin/env python3
islower = __import__('7-islower').islower


def islower(c):
    return ord('a') <= ord(c) <= ord('z')
