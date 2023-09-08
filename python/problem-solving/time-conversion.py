#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    numHour = int(s[:2])
    if s[-2:] == 'AM':
        if (numHour % 12) == 0:
            numHour %= 2
    else:
        if numHour < 12:
            numHour += 12
    return str(numHour).zfill(2) + s[2:-2]

if __name__ == '__main__':
    # https://stackoverflow.com/questions/52760487/python-keyerror-output-path
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
