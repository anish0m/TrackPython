# solution by anish0m



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = ""
    nxt = True
    
    for c in s:
        if c==" ":
            result += c
            nxt = True
        elif nxt:
            nxt = False
            result += c.upper()
        else:
            result += c
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
