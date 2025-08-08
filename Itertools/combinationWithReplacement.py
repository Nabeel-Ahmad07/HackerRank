# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

string, n = input().split()
n = int(n)
string = ''.join(sorted(string))

for i in combinations_with_replacement(string,n):
    print(''.join(i))