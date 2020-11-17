import math
import os
import random
import re
import sys

###############TODO
# Complete the countInversions function below.
def countInversions(arr):
    length = len(arr)
    new_array = list(range(length + 1))
    count = 0
    for i in range(length + 1):
        # value = arr[i]
        # position = new_array.index(value)
        # count += (i - position)
        min_value = min(arr)
        value_index = arr.index(min_value)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
