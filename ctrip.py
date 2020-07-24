#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    dict = {}
    dictpairs = {}
    for i in reversed(arr):
        if i*r in dictpairs:
            count += dictpairs[i*r]
        if i*r in dict:
            dictpairs[i] = dictpairs.get(i, 0) + dict[i*r]

        dict[i] = dict.get(i, 0) + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
