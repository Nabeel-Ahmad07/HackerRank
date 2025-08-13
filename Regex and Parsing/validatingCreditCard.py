# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^(?!.*(\d)(?:-?\1){3})(?:[456]\d{15}|[456]\d{3}(?:-\d{4}){3})$'

for _ in range(int(input())):
    text = input().strip()
    if re.match(pattern, text):
        print("Valid")
    else:
        print("Invalid")