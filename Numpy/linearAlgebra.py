import numpy



N = int(input())

A=[]
for _ in range(N):
    row = list(map(float, input().split()))
    A.append(row)
    

print(round(numpy.linalg.det(A), 2))
