import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    n_list = [0] * (n + 1)
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        for i in range(a, b + 1):
            n_list[i] += k
    return max(n_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
