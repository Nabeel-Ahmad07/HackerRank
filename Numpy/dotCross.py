import numpy

N = int(input())

A=[]
for _ in range(N):
    row= list(map(int, input().split()))
    A.append(row)
    
B=[]
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
A = numpy.array(A)
B = numpy.array(B)

print(numpy.dot(A,B))
