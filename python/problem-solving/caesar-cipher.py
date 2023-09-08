#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = ''
    alphabetLength = len(alphabet)
    for i in range(alphabetLength):
        newIdx = (i + k) % alphabetLength
        shifted += alphabet[newIdx]
    
    ciphertext = ''
    for j in range(len(s)):
        if not(s[j].isalpha()):
            ciphertext += s[j]
            continue
        originalIdx = alphabet.index(s[j].lower())
        ciphertext += shifted[originalIdx].upper() if s[j] == s[j].upper() else shifted[originalIdx]
    return ciphertext

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
