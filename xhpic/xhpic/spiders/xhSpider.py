import scrapy
from scrapy.http import Request
from xhpic.items import XhpicItem
import time

class XhSpider(scrapy.Spider):
    name = 'xh_spider'
    allowed_domain = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html']
    
    def parse(self, response):
        lists = response.xpath('//div[@class="img"]/a')
        for person in lists:
            item = XhpicItem()
            item['name'] = person.xpath('./img/@alt').extract()[0]
            item['addr'] = person.xpath('./img/@src').extract()[0]
            item['addr'] = 'http://www.xiaohuar.com' + item['addr']
            print item
            yield item

            # urls = ['http://www.xiaohuar.com/list-1-{}.html'.format(i) for i in range(1,44)]
            # for url in urls:
            #     yield Request(url,callback = self.parse)
            