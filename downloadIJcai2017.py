# -*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
path = "C:\\Users\\NLSDE\\Desktop\\"
#以下是Python2.x爬取
#由于accept paper页面无法爬取，看到里面涉及到读取json，找到json数据来源，这里读取json将论文题目与作者写入文件

url = path+"ijcai-accept.json"
with open(path+"2017_acceptedPaper_IJCAI.csv","w") as f:
    i = 0
    f.write("index,PaperID,Title,Authors\n")
    with open(url, 'r') as f2:
        items = json.load(f2)
    for item in items:
        i += 1
        f.write(str(i) + "," + str(item['paperID']) +","+str(item['title'])+","+str(item['authors']).replace(",","#")+"\n")