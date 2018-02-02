# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from duanzi.items import DuanziItem

class duanziSpider(scrapy.Spider):
	name = 'duanzi_spider'
	allowed_domains = ['duanziwang.com']
	start_urls = ['https://duanziwang.com/page/1']

	def parse(self,response):
		lists = response.xpath('//div[@class="content"]/article')
		tempContent = None
		for each in lists:
			item = DuanziItem()
			item['title'] = each.xpath('./header/h2/a/text()').extract()[0]
			tempContent = each.xpath('./p[@class="note"]/text()')
			if len(tempContent) > 0:
				item['content'] = tempContent.extract()[0]
			else:
				item['content'] = 'No desc content'

			item['info'] = each.xpath('./p[@class="text-muted time"]/text()').extract()[0]
			print item
			yield item

		urls = ['https://duanziwang.com/page/{}'.format(str(i)) for i in range(2,102)]
		for url in urls:
			yield Request(url,self.parse)
