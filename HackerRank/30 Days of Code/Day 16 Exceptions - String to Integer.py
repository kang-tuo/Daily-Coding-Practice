#!/bin/python3

import sys


S = input().strip()
try:
    int_value=int(S)
    print(int_value)
except:
    print("Bad String")
