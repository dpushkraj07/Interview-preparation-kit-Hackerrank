#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):

    moves = 0
    for i in range(len(Q)-1,0,-1):
        if Q[i] != i+1:
            if Q[i-1] == i+1:
                moves+=1
                Q[i],Q[i-1] = Q[i-1],Q[i]
            elif Q[i-2] == i+1:
                moves+=2
                Q[i-2],Q[i-1] = Q[i-1],Q[i-2]
                Q[i-1],Q[i] = Q[i],Q[i-1]
            else:
                print("Too chaotic")
                return
    print(moves)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
