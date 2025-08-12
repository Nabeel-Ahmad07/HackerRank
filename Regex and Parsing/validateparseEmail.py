# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
N = int(input())
pattern = r'^[A-Za-z][\w\.-]*@[A-Za-z]+\.[A-Za-z]{1,3}$'

for _ in range(N):
    nameA, emailA = email.utils.parseaddr(input())
    
    if re.match(pattern, emailA):
        print(email.utils.formataddr((nameA, emailA)))