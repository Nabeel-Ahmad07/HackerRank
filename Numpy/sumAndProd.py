import numpy


N, M = map(int, input().split())

rList = []
for _ in range(N):
    arr = list(map(int, input().split()))
    rList.append(arr)
    
my_array = numpy.array(rList)
x = numpy.sum(my_array, axis=0)
print(numpy.prod(x))