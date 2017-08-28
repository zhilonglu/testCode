# -*- coding: utf-8 -*-
import traceback
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import random

# 存储为文本的子函数
def write2txt(data,path):
    f = open(path,"a")
    f.write(data)
    f.write("\n")
    f.close()
# 获取该id喜欢音乐的列表
def catchSongs(url_id,url):
    user = url_id.split('=')[-1].strip()
    print('excute user:',user)
    driver = webdriver.PhantomJS(
    executable_path="C:\\Users\\NLSDE\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    #  注意填上路径
    driver.get(url)
    driver.switch_to_frame('g_iframe')  # 网易云的音乐元素都放在框架内！！！！先切换框架
    try:
        wait = ui.WebDriverWait(driver,15)
        wait.until(lambda driver: driver.find_element_by_xpath('//*[@class="j-flag"]/table/tbody'))
        # 等待元素渲染出来
        try:
            song_key = 1
            wrong_time = 0
            while wrong_time < 5:  # 不断获取歌信息，假定5次获取不到值，就判无值可获取，跳出循环
                try:
                    songs = driver.find_elements_by_xpath('//*[@class="j-flag"]/table/tbody/tr[%s]'%song_key)
                    info_ = songs[0].text.strip().split("\n")
                    if len(info_) == 5:
                        info_.insert(2,'None') # 没有MV选项的进行插入None
                    new_line = '%s|'%user+'|'.join(info_)
                    song_key +=1
                    print(new_line)
                    write2txt(new_line.encode('utf-8'),user)
                except Exception as ex:
                    wrong_time +=1
                    # print ex
        except Exception as ex:
            pass
    except Exception as ex:
        traceback.print_exc()
    finally:
        driver.quit()

# 获取id所喜爱的音乐的url
def catchPlaylist(url):
    driver = webdriver.PhantomJS(
        executable_path="C:\\Users\\NLSDE\\Downloads\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    #  注意填上路径
    driver.get(url)
    driver.switch_to_frame('g_iframe')  # 网易云的音乐元素都放在框架内！！！！先切换框架
    try:
        wait = ui.WebDriverWait(driver,15)
        wait.until(lambda driver: driver.find_element_by_xpath('//*[@class="m-cvrlst f-cb"]/li[1]/div/a'))
        # 根据xpath获取元素
        urls = driver.find_elements_by_xpath('//*[@class="m-cvrlst f-cb"]/li[1]/div/a')
        favourite_url = urls[0].get_attribute("href")
    except Exception as ex:
        traceback.print_exc()
    finally:
        driver.quit()
    # print favourite_url
    return favourite_url

if __name__ == '__main__':
    for url in ['http://music.163.com/#/user/home?id=91575734']:
        # 这里把自己的id替换掉，想爬谁的歌单都可以，只要你有他的id
        time.sleep(random.randint(2, 4)) # 随机休眠时间2~4秒
        # url_playlist = catchPlaylist(url)
        url_id = 'id=91575734'
        catchSongs(url_id, url)
        time.sleep(random.randint(1, 2))