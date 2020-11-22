#!/bin/python3

import math
import os
import random
import re
import sys


def get_max_sum(arr):
    sums = []
    for i in range(1, 5):
        for j in range(1, 5):
            a = arr[i - 1][j - 1]
            b = arr[i - 1][j]
            c = arr[i - 1][j + 1]
            d = arr[i][j]
            e = arr[i + 1][j - 1]
            f = arr[i + 1][j]
            g = arr[i + 1][j + 1]
            num_sum = a + b + c + d + e + f + g
            sums.append(num_sum)

    return max(sums)


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    print(get_max_sum(arr))
