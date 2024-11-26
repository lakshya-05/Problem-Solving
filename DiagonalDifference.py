# DiagonalDifference.py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(n, arr):
    # Write your code here
    res1 = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                res1 = res1 + arr[i][i]

    res2 = 0
    for i in range(n):
        for j in range(n):
            if i == n-1-j:
                res2 = res2 + arr[i][j]

    res = res1 - res2
    res = res**2
    res = res**(0.5)

    return int(res)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n, arr)
    print(result)
