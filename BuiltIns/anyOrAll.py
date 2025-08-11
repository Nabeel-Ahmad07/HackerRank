# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
rlist = list(map(int, input().split()))

positive = all(num > 0 for num in rlist)
palindrome = any(str(num) == str(num)[::-1] for num in rlist)


print(positive and palindrome)