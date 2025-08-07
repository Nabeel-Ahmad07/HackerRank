# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input())
bc = int(input())

radians = math.atan2(ab, bc)     
degree = round(math.degrees(radians)) 

print(f"{degree}\u00B0")
