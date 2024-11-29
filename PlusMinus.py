#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    pos_new = pos / (pos + neg + zero)
    print("%0.6f" % pos_new)
    neg_new = neg / (pos + neg + zero)
    print("%0.6f" % neg_new)
    zero_new = zero / (pos + neg + zero)
    print("%0.6f" % zero_new)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
    #print(len(arr))
