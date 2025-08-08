# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
l = list(input().split())
k = int(input())
count = 0         

for i in combinations(l,k):
    if 'a' in i:
        count += 1

totalCombos = len(list(combinations(l,k)))
print(count/totalCombos)