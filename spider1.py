# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def sexjudgement(class_name):
    if class_name == 'member_ico':
        return '男'
    else:
        return '女'

def get_url(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        get_info(link.get('href'))

def get_info(url):
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    
    titles = soup.select('.pho_info > h4 > em')
    addresses = soup.select('.pho_info > p > span.pr5')
    prices = soup.select('#pricePart > .day_l > span')
    imgs = soup.select('.member_pic > a > img')
    names = soup.select('.js_box > a.lorder_name')
    sexs = soup.select('.member_pic > div.member_ico')
    
    for title,address,price,img,name,sex in zip(titles,addresses,prices,imgs,names,sexs):
        data = {
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'img':img.get('src'),
            'name':name.get_text(),
            'sex':sexjudgement(sex.get('class'))
        }
        print data
    

if __name__ == '__main__':
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(0,1)]
    for url in urls:
        get_url(url)
        time.sleep(60)