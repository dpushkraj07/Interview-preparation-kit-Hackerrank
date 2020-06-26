#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a = 0
    ns = ''
    ss = ''
    for i in s:
        if i == 'a':
            a+=1

    fd = n // len(s)

    a = a * fd
    r = n % len(s)
    ss = s[:r]
    for i in ss:
        if i == 'a':
            a += 1

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
