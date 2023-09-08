#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = -math.inf
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            # print('Considered rows and columns', i, j)
            hourglass_sum = calcHourglass(arr, i, j)
            if hourglass_sum > max_sum:
                # print('New maximum! ', hourglass_sum)
                max_sum = hourglass_sum
    return max_sum

def calcHourglass(arr, r, c):
    total_hourglass = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0) and ((j == -1) or (j == 1)):
                # print('i and j when true', i, j)
                continue
            total_hourglass += arr[r + i][c + j]
            # print('CALCULATING SUM for', r+i, c+j, ': ', total_hourglass)
    # print('SUM CALCULATED: ', total_hourglass)
    return total_hourglass
            
if __name__ == '__main__':
    # https://stackoverflow.com/questions/52760487/python-keyerror-output-path
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
