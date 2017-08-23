# -*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib
import re
from bs4 import BeautifulSoup
path = "C:\\Users\\NLSDE\\Desktop\\"
result = []
rooturl = "http://offernews.cn" #爬取网站中所有的IT公司以及招聘岗位

def readContent(url,result):
    content = urllib.urlopen(url).read()
    soup=BeautifulSoup(content,"html.parser")
    tr = soup.find_all("tr","offertr")
    for i in range(len(tr)):
        company = tr[i].contents[1].string
        location = tr[i].contents[3].string
        job = tr[i].contents[5].string
        time = tr[i].contents[7].string
        salaryurl = tr[i].contents[9].contents[0]['href']
        content = urllib.urlopen(rooturl+salaryurl).read()
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find_all("table", "table table-bordered")
        for j in table:
            salary = j.contents[5].contents[2].string
            package = j.contents[7].contents[2].string
            if package == None:
                package = "无"
            else:
                package = package.replace(",","#")
        result.append(company+","+location+","+job+","+salary+","+package+","+time)
    print(len(result))
    return result

result = readContent(rooturl,result)
page = 2
while page<7:
    url = rooturl + "/?pageIndex="+str(page)
    print(url)
    result = readContent(url,result)
    page += 1
print(len(result))
with open(path+"IDcompany.csv","w") as f:
    f.write("公司"+","+"工作地点"+","+"职位"+","+"月薪"+","+"package"+","+"获得时间"+"\n")
    for i in result:
        f.write(i+"\n")