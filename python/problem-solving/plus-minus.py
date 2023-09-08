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
    numPos, numNeg, numZero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            numPos += 1
        elif arr[i] < 0:
            numNeg += 1
        else:
            numZero += 1
    print('{:.6f}'.format(numPos / len(arr)))
    print('{:.6f}'.format(numNeg / len(arr)))
    print('{:.6f}'.format(numZero / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
