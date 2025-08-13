# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$'

for _ in range(int(input())):
    text = input()
    if re.match(pattern, text):
        print("Valid")
    else:
        print("Invalid")
    