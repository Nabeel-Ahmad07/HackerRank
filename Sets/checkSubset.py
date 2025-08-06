# Enter your code here. Read input from STDIN. Print output to STDOUT
n  = int(input())

for _ in range(n):
    x = int(input())
    x_set = set(map(int, input().split()))
    y = int(input())
    y_set = set(map(int, input().split()))
    
    if x_set.issubset(y_set):
        print("True")
    else:
        print("False")
