#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    # Declare a 2-dim array of n empty arrays
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    for i in range(len(queries)):
        x = queries[i][1]
        y = queries[i][2]
        idx = ((x ^ lastAnswer) % n)
        if queries[i][0] == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
    return answers

if __name__ == '__main__':
    # https://stackoverflow.com/questions/52760487/python-keyerror-output-path
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
