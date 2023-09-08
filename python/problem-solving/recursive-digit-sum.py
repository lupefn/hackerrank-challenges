#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    sumDigits = sum(map(int, list(n))) # sum all of the digits
    sumMultK = sumDigits * k # multiply by k to get total digits
    # if the length of that multiplication is greater than 1 then we have to keep calling our function recursively
    return sumMultK if len(str(sumMultK)) == 1 else superDigit(str(sumMultK), 1)
    
    # original solution
    # print(n)
    # print(list(n))
    # if len(n) == 1:
    #     print('returning')
    #     return n
    # p = n * k
    # print('p', p)
    # sumOfPValues = sum(map(int, p))
    # return superDigit(str(sumOfPValues), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
