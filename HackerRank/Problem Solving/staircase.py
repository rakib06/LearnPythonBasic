#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        print(' ' * ((n - i) - 1) + '#' * (i + 1))


def miniMaxSum(arr):
    arr.sort()
    print(arr)
    n = len(arr)
    maxSum, minSum = 0,0
    for i in range(n - 4, n):
        maxSum += arr[i]
    for i in range(0, 4):
        minSum += arr[i]

    print(maxSum,minSum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

'''
if __name__ == '__main__':
    n = int(input())

    staircase(n)
'''