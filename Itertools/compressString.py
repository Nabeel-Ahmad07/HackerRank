# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = list(map(int, input()))

for key,group in groupby(s):
    print(f"({len(list(group))}, {key})", end=" ")
