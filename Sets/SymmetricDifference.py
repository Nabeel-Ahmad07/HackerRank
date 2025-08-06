# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
setA = set(map(int, input().split()))
N = int(input())
setB = set(map(int, input().split()))

x = setA.difference(setB)
y =  setB.difference(setA)

z = sorted(x.union(y))

for i in range(len(z)):
    print(z[i])
