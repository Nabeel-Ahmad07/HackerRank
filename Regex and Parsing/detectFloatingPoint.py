# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
pattern = re.compile(r'^[+-]?\d*\.\d+$')

for _ in range(T):
    N = input()
    
    if pattern.match(N):
        print(True)
    else:
        print(False)