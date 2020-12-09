#!/bin/python3

import math
import os
import random
import re
import sys


def if_gmail(email):
    at_index = email.index("@")
    string_after_at = email[at_index + 1:at_index + 6]
    if string_after_at == "gmail":
        return True
    return False


if __name__ == '__main__':
    N = int(input())

    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if if_gmail(emailID):
            names.append(firstName)

    names.sort()
    for name in names:
        print(name)
