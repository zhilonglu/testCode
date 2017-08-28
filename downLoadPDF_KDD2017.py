# -*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import re
from bs4 import BeautifulSoup
path = "C:\\Users\\NLSDE\\Desktop\\"
#以下是Python2.x爬取

url = "http://www.kdd.org/kdd2017/accepted-papers"
content = urllib.urlopen(url).read()
soup=BeautifulSoup(content,"html.parser")
htmls = soup.find_all(href=re.compile("http://www.kdd.org/kdd2017/papers/*"))
with open(path+"2017_acceptedPaper.csv","w") as f:
    i = 0
    f.write("index,paper_name\n")
    for item in htmls:
        i += 1
        f.write(str(i) + "," + str(item.string).replace(":","_").replace(",","_").replace("?","").replace("&nbsp;"," ") + "\n")