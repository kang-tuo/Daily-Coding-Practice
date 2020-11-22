#!/bin/python3

import math
import os
import random
import re
import sys


w="Weird"
nw="Not Weird"

def if_wierd(N):
    if N%2 !=0:
        return w
    else:
        if N>= 6 and N<=20:
            return w
        else:
            return nw

if __name__ == '__main__':
    N = int(input())
    result=if_wierd(N)
    print(result)
