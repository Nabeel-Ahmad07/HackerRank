# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = map(int, input().split())

lists = []
for _ in range(k):
    l = list(map(int, input().split()))[1:]
    lists.append(l)
    
maxVal = 0
for i in product(*lists):
    total = sum(x**2 for x in i) %m
    if total > maxVal:
        maxVal = total
        
print(maxVal)
