#coding=utf-8
import re
import sys

from util import *

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = r"E:\git_project\python_project\txtToHtml\test_input.txt"
htmlFileName = r"E:\git_project\python_project\txtToHtml\test_input.html"

htmlFile = open(htmlFileName, "w+")
file = open(filename)
htmlFile.write("<html><head><title>...</title></head><body>")

title = True
for block in blocks(file):
    block = re.sub(r'\*(.+?)\*', r'<em>\g<1></em>', block)  #\g<1>表示group1 匹配字符串
    if title:
        htmlHead = '<h1>' + block + '</h1>'
        title = False
        htmlFile.write(htmlHead)
    else:
        htmlBody = '<p>' + block + '</p>'
        htmlFile.write(htmlBody)
htmlFile.write( "</body></html>")

htmlFile.close()
file.close()