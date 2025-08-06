# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

x = A.union(B)

count = 0
for item in x:
    count += 1
    
print(count)
