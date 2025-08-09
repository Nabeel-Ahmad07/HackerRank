# !/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

counts = {}

for alphabet in s:
    if alphabet in counts:
        counts[alphabet] += 1
    else:
        counts[alphabet] = 1
    
    
items = list(counts.items())
items.sort(key=lambda x: (-x[1], x[0]))

for i in range(3):
    print(items[i][0], items[i][1])
    