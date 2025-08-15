import numpy



N, M = map(int, input().split())

rList = []
for _ in range(N):
    arr = list(map(int, input().split()))
    rList.append(arr)
    
myArray = numpy.array(rList)
print(numpy.transpose(myArray))
print(myArray.flatten())
