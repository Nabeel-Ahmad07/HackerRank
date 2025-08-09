# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)

A,B = input().split()
A, B = int(A), int(B)

for i in range(1, A + 1): 
    word = input()
    d[word].append(i)
    
for _ in range(B):
    word = input()
    if word in d:
        print(*d[word])
    else:
        print(-1)