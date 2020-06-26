#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0
    if (len(c)-2) == 0:
        return 1
    while i<(len(c)-2):
        if c[i+1] == 0 and c[i+2] == 0:
            i = i + 2
            count +=1
        elif c[i+1] == 0 and c[i+2] == 1:
            i += 1
            count += 1
        elif c[i+1] == 1 and c[i+2] == 0:
            i = i + 2
            count += 1

    if c[n-3] != 0:
        if c[n-1] == 0 and c[n-2] == 0:
            count+=1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
