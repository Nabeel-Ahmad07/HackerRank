# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
Sizes = list(map(int, input().split()))

stock = Counter(Sizes)

amout = 0

N = int(input())
for _ in range(N):
    size, prize = map(int, input().split())
    
    if stock[size] > 0:
        amout += prize
        stock[size] -= 1
        
print(amout)