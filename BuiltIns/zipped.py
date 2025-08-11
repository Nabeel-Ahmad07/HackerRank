# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
rlist = []
for _ in range(X):
    A = list(map(float, input().split()))
    rlist.append(A)


for marks in zip(*rlist):
    print(sum(marks)/X)