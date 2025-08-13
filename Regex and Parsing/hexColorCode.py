# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

css = "\n".join(input() for _ in range(n))

    
blocks = re.findall(r'\{([^}]*)\}', css)

matches = []
pattern = r'#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b'
for block in blocks:
    codes = re.findall(pattern, block)
    matches.extend(codes)

for m in matches:
    print(m)