#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    dic = Counter()

    dict_val = Counter()

    arr = []

    for q in queries:
        if q[0]==1:
            dict_val[dic[q[1]]]-=1
            dic[q[1]]+=1
            dict_val[dic[q[1]]]+=1

        elif q[0]==2:
            if dic[q[1]]>0:
                dict_val[dic[q[1]]]-=1
                dic[q[1]]-=1
                dict_val[dic[q[1]]]+=1

        else:
            if dict_val[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)

    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
