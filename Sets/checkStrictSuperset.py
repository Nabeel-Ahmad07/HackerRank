# Enter your code here. Read input from STDIN. Print output to STDOUT
A_set = set(map(int, input().split()))

n = int(input())
is_strictSuperset = True

for _ in range(n):
    x = set(map(int, input().split()))
    if not (A_set > x):
        is_strictSuperset = False
        break

print(is_strictSuperset)
