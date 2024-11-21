#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice = 0
    bob = 0
    arr = list()
    for i in range(3):
        if a[i] > b[i]:
            alice = alice + 1
        elif a[i] < b[i]:
            bob = bob + 1
        elif a[i] == b[i]:
            pass
    arr.append(alice)
    arr.append(bob)
    return arr


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
