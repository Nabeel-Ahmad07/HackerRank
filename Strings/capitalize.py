#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = ''
    capitalize = True 

    for char in s:
        if char.isalpha() and capitalize:
            result += char.upper()
            capitalize = False
        else:
            result += char
            if char == ' ':
                capitalize = True
            else:
                capitalize = False

    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
