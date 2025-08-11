# Enter your code here. Read input from STDIN. Print output to STDOUT
X = sorted(input())
upperCase = []
lowerCase = []
even = []
odd = []

for char in X:
    if char.islower():
        lowerCase.append(char)
    elif char.isupper():
        upperCase.append(char)
    elif char.isdigit():
        if int(char)%2 == 1:
            odd.append(char)
        else:
            even.append(char)
            
result = "".join(lowerCase+upperCase+odd+even)
print(result)
