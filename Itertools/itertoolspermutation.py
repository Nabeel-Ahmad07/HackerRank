# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string, n = input().split()
n = int(n)
string = ''.join(sorted(string))

for i in permutations(string, n):
    print("".join(i))