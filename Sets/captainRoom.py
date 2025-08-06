# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
room = list(map(int, input().split()))
room_set = set(room)

a = sum(room_set)
b = sum(room)

print((K * a - b) // (K - 1))
