# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime

month, date, year = map(int, input().split())

day = datetime(year, month, date)
dayName = day.strftime("%A").upper()
print(dayName)