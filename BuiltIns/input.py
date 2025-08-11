# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, input().split())

Eq = input()

if eval(Eq) == k:
    print(True)
else:
    print(False)