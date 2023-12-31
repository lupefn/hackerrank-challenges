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

def diagonalDifference(arr):
    # Write your code here
    primary = 0
    secondary = 0
    for i in range(len(arr[0])):
        primary += arr[i][i]
        secondary += arr[len(arr[0]) - i - 1][i]
    return abs(primary - secondary)    

if __name__ == '__main__':
    # https://stackoverflow.com/questions/52760487/python-keyerror-output-path
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
