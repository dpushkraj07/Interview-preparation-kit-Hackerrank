#!/bin/python3

import math
import os
import random
import re
import sys


def sherlockAndAnagrams(string):
    buckets = {}
    c = 0
    for i in range(len(string)):
        for j in range(len(string) - i):
            key = ''.join(sorted(string[i:i+j+1]))
            buckets[key] = buckets.get(key, 0) + 1
            c+=buckets[key]-1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
