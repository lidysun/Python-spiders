# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

#爬取酷狗音乐Top 500
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_songs(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    
    names = soup.select('#rankWrap > .pc_temp_songlist > ul > li > .pc_temp_songname')
    indexs = soup.select('#rankWrap > .pc_temp_songlist > ul > li > .pc_temp_num')

    for name,index in zip(names,indexs):
        data = {
            'name':name.get_text().strip(),
            'index':index.get_text().strip()
        }
        print data


if __name__ == '__main__':
    # 500/22 = 23.x
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(page) for page in range(1,24)]
    for url in urls:
        get_songs(url)
        time.sleep(2)

