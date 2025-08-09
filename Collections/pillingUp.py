# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T = int(input())


for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split())) 
    
    currmax = float('inf')
    possibility = True
    
    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.popleft()
        else:
            pick = cubes.pop()
        
        
        if pick <= currmax:
            currmax = pick
        else:
            possibility = False
            break
            
            
    if possibility:
        print("Yes")
    else:
        print("No")
