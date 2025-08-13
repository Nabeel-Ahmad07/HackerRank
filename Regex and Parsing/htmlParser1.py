# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

n = int(input())
html = "\n".join(input() for _ in range(n))

html = re.sub(r'<!--[\s\S]*?-->', '', html)

parser = MyHTMLParser()
parser.feed(html)