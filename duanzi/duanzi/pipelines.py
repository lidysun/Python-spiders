# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DuanziPipeline(object):
    def process_item(self, item, spider):
    	with open('duanzi.txt','a+') as fp:
    		fp.write(item['title'] + '\n')
    		fp.write(item['content'] + '\n')
    		fp.write(item['info'] + '\n\n')
    	return item
