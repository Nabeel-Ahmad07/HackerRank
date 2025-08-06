# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    cmd = input().split()
    op = cmd[0]
    
    other_set = set(map(int, input().split()))
    
    if cmd[0] == "intersection_update":
        A.intersection_update(other_set)
    elif cmd[0] == "update":
        A.update(other_set)
    elif cmd[0] == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
    elif cmd[0] == "difference_update":
        A.difference_update(other_set)
        
print(sum(A))
