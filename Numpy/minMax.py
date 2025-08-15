import numpy



N, M = map(int, input().split())
rows = []

for _ in range(N):
    row = list(map(int, input().split()))
    rows.append(row)

my_array = numpy.array(rows)
x = numpy.min(my_array, axis=1)

print(numpy.max(x, axis=None))
