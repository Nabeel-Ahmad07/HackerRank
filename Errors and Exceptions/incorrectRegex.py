import re
possessive_pattern = r'(?:[*+?]|\{\d+(?:,\d*)?\})\+'

for _ in range(int(input())):
    pattern = input().strip()
    if re.search(possessive_pattern, pattern):
        print("False")
    else:
        try:
            re.compile(pattern)
            print("True")
        except re.error:
            print("False")

#solved with help of GPT