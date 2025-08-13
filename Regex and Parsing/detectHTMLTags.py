# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)
            
parser = MyHTMLParser()

n = int(input())
for _ in range(n):
    text = input()
    parser.feed(text)   