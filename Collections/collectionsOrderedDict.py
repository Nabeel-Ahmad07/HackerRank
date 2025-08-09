# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = OrderedDict()

N = int(input())

for _ in range(N):
    *nameChunks, price = input().split()
    name = ' '.join(nameChunks)
    price = int(price)
    
    if name in items:
        items[name] += price
    else: 
        items[name] = price
    
for name, totalPrice in items.items():
    print(name, totalPrice)