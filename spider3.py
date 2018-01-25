# -*- coding: utf-8 -*-
import re
import requests
import time


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
f = open('斗破苍穹.txt'.decode('utf-8'),'a+')

def get_info(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',response.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(' ' + content + '\r\n')
    else:
        pass

if __name__ == '__main__':
    for i in range(1,100):
        url = 'http://www.doupoxs.com/doupocangqiong/'+ str(i) +'.html'
        print '第'+ str(i) + '页抓取中...'
        get_info(url)
        time.sleep(2)

f.close()
