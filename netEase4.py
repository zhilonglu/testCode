# -*- coding:utf-8 -*-
# 调用的阿里云的API接口实现语种翻译
# API官网：https://market.aliyun.com/products/57124001/cmapi010395.html?spm=5176.730005.0.0.UrR9bO#sku=yuncode439500000
import urllib, urllib2
import ssl
import json

def Lang2Country(text):
    host = 'https://dm-12.data.aliyun.com'
    path = '/rest/160601/mt/detect.json'
    method = 'POST'
    appcode = 'xxxxx'  # 购买后提供的appcode码
    querys = ''
    bodys = {}
    url = host + path
    bodys['q'] = text
    post_data = urllib.urlencode(bodys)
    request = urllib2.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    # 根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib2.urlopen(request, context=ctx)
    content = response.read()
    if (content):
        # print(content)
        return content
    else:
        return None
#
# 67259702|1|Claux - 水之畔(8lope Remix) (feat. 陶心瑶)|None|02:44|8lope|水之畔(feat. 陶心瑶) (8lope Remix)
list_songs = []
list_songwithsinger = []
with open('67259702') as f:  # 文件名写上次爬下来的
    for line in f:
        line_split = line.split('|')
        list_songs.append(line_split[2])
        list_songwithsinger.append(line_split[2]+line_split[5])


# 调用接口进行语种识别
dict_lang = {}
for i in range(537):
    try:
        content = Lang2Country(list_songwithsinger[i])
        lag_ = json.loads(content)['data']['language']
        if lag_ not in dict_lang:
            dict_lang[lag_]=0
        dict_lang[lag_] +=1
    except:
        pass
print(dict_lang)

# {u'ru': 1, u'fr': 9, u'en': 111, u'zh': 259, u'pt': 21, u'ko': 8, u'de': 7, u'tr': 15, u'it': 47, u'id': 2, u'pl': 7, u'th': 1, u'nl': 10, u'ja': 17, u'es': 20}