# -*-coding:utf-8-*-
import urllib
#下面是Python3.x读取网页内容的代码
# url = 'http://proceedings.mlr.press/v70/jaderberg17a/jaderberg17a.pdf'
# #first way to get download
# print("downloading with urllib")
# urllib.request.urlretrieve(url, "C:\\Users\\NLSDE\\Desktop\\1.pdf")
# # #second way to get download
# # print("downloading with urllib2")
# # f = urllib.request.urlopen(url)
# # data = f.read()
# # with open("code2.zip", "wb") as code:
# #     code.write(data)

#以下代码是Python2.x读取知乎网站并下载页面上所有图片的Python代码
from sgmllib import SGMLParser

class ZhihuParser(SGMLParser):
    imgList = []

    def reset(self):
        SGMLParser.reset(self)  # 初始化
        self.imgList = []

    def start_img(self, attrs):
        imgUrl = [v for k, v in attrs if k == 'data-original']
        if imgUrl:
            self.imgList.append(imgUrl[0])
            imgUrl = ""

url = "https://www.zhihu.com/question/20922273"
page = urllib.urlopen(url)
parser = ZhihuParser()
parser.feed(page.read())
# print(parser.imgList)
cnt = 1
for url in parser.imgList:
    f = open("%d.jpg"%cnt,'wb')
    img = urllib.urlopen(url)
    f.write(img.read())
    f.close()
    print("%d was done!"%cnt)
    cnt += 1