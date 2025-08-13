# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)