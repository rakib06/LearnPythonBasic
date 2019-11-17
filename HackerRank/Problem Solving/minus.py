#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    zero = 0
    positive = 0
    neg = 0
    for i in range(n):
        for item in range(n):
            if arr[i][j] < 0:
                neg+=1
            elif arr[j][j] == 0:
                zero += 1
            else:
                positive +=1
    print(positive)
    print(neg)
    print(zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
