#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(' ')

    print(s)
    for i in range(len(s)):
        if s[i] == '':
            r += ' '
        else:
            print(str(s[i][0]).upper()+s[i][1:], end=' ')


solve('hello   world  lol')

'''
# Submitted code 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    r = ''
    for i in range(len(s)):
        if s[i] == '':
            r += ' '
        else:
            r += str(s[i][0]).upper()+s[i][1:]+' '
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


'''

