# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
d = {}

for _ in range(n):
    word = input()
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
        
print(len(d))
print(*d.values())