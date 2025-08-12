# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
m = re.compile(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])")

matches = m.findall(s)
if matches:
    for item in matches:
        print(item)
else:
    print("-1")