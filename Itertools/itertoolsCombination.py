# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string, n = input().split()
n = int(n)

string = ''.join(sorted(string))

for i in range(1, n + 1):
    for j in combinations(string, i):
        print(''.join(j))