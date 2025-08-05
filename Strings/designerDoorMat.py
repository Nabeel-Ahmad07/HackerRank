# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = map(int, input().split())

for i in range(1, a, 2):
    pattern = (".|." * i).center(b, "-")
    print(pattern)
    
print("WELCOME".center(b, "-"))

for i in range(a-2,0,-2):
    pattern = (".|." * i).center(b, "-")
    print(pattern)
