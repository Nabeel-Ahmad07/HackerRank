# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())

header = input().split()
Student = namedtuple('Student', header)
totalMarks = 0
for _ in range(N):
    values = input().split()
    student = Student(*values)
    
    totalMarks += int(student.MARKS)
    
print(totalMarks/N)
    