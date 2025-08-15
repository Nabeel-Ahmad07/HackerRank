import numpy

N, M = map(int, input().split())
rows = []

for _ in range(N):
    row = list(map(int, input().split()))
    rows.append(row)

my_array = numpy.array(rows)

print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))

std = numpy.std(my_array)
print(float(f"{std:.11f}"))
