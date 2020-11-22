#!/bin/python3

import math
import os
import random
import re
import sys


def reversed_arr(arr):
    arr_len = len(arr)
    result = ""
    for i in range(arr_len):
        result = result + str(arr[arr_len - i - 1]) + " "
    print(result[:len(result) - 1])


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reversed_arr(arr)
