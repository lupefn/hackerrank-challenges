#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(line):
    start = 0
    end = len(line) - 1
    while ((start < end) and (line[start] == line[end])):
        start += 1
        end -= 1
    # print('start', start)
    # print('end', end)
    if start >= end:
        return -1
    if isPalindrome(line, start, end-1):
        return end
    if isPalindrome(line, start+1, end):
        return start
    return -1

def isPalindrome(line, s, e):
    # print('Line:', line[s:e+1])
    # print('Line reversed:', line[s:e+1][::-1])
    return line[s:e+1] == line[s:e+1][::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
