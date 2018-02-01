# -*- coding: utf-8 -*-
import urllib2
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XhpicPipeline(object):
    def process_item(self, item, spider):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        req = urllib2.Request(url = item['addr'],headers = headers)
        res = urllib2.urlopen(req)
        file_name = os.path.join(r'D:\project\WWW\xhpic\download_pic',item['name'] + '.jpg')
        with open(file_name,'wb') as fp:
            fp.write(res.read())
