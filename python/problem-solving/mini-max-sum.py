#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    overallMin = math.inf
    overallMax = -math.inf
    for i in range(len(arr)):
        total = sum(arr[0:i]) + sum(arr[i+1:len(arr)+1])
        if total > overallMax:
            overallMax = total
        if total < overallMin:
            overallMin = total
    print(overallMin, overallMax)

##alt one-liner solution
##print(sum(sorted(input_list)[:-1]), sum(sorted(input_list[1:])))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
