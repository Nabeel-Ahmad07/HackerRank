import numpy



coeffs = list(map(float, input().split()))

x = float(input())

print(numpy.polyval(coeffs, x))
