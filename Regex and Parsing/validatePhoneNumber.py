# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
pattern = r"^[789]\d{9}$"
for _ in range(N):
    M = input()
    if re.match(pattern, M):
        print("YES")
    else:
        print("NO")