from bs4 import BeautifulSoup
import re
import urllib
doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
# soup = BeautifulSoup(''.join(doc))
# # print(soup.prettify())
# print(soup.contents[0].name)

url = "http://proceedings.mlr.press/v70/"
content = urllib.urlopen(url).read()
soup=BeautifulSoup(content,"html.parser")
# print(soup.prettify())
# print(soup.contents[0])
body = soup.find_all("p","links")
title = soup.find_all("p","title")
print(len(title))
print(title[0].string)

div = soup.find_all("div","paper")
print(len(div))
# print(div[0])
html = soup.find_all(href=re.compile("http://.*17[a-z].pdf"))
print(len(html))
print(html[0]['href'])
# html_pdf = re.findall("http://.*17a.pdf",str(html[0]))
# print(html_pdf[0])
# header = body
# print(header)