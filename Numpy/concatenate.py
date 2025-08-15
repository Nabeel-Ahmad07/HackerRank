import numpy



N,M,P = map(int, input().split())
nList = []
for _ in range(N):
    nList.append(list(map(int, input().split())))
    
mList = []
for _ in range(M):
    mList.append(list(map(int, input().split())))
    
print(numpy.concatenate((numpy.array(nList), numpy.array(mList))))
