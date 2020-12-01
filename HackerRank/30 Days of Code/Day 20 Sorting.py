#!/bin/python3

import sys

# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
n = 3
a = [3, 2, 1]

numberOfSwaps = 0


def swap(a, j):
    b = a.copy()
    b[j] = a[j + 1]
    b[j + 1] = a[j]
    return b


for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a=swap(a, j)
            numberOfSwaps += 1

    if (numberOfSwaps == 0):
        break

print("Array is sorted in %d swaps." % numberOfSwaps)
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
