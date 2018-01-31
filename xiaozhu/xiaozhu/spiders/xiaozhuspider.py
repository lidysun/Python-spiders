# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from xiaozhu.items import XiaozhuItem

class xiaozhu(CrawlSpider):
    name = 'xiaozhu'
    start_urls = ['http://wh.xiaozhu.com/fangzi/19739088603.html']
    
    def parse(self,response):
        item = XiaozhuItem()
        selector = Selector(response)
        
        title = selector.xpath('//h4/em/text()').extract()[0].strip()
        address = selector.xpath('//div[@class="pho_info"]/p/span[@class="pr5"]/text()').extract()[0].strip()
        price =selector.xpath('//div[@id="pricePart"]/div/span/text()').extract()[0]
        lease_type =selector.xpath('//*[@id="introduce"]/li[1]/h6/text()').extract()[0]
        suggestion =selector.xpath('//*[@id="introduce"]/li[2]/h6/text()').extract()[0]
        bed =selector.xpath('//*[@id="introduce"]/li[3]/h6/text()').extract()[0]
        
        item['title'] = title
        item['address'] = address
        item['price'] = price
        item['lease_type'] = lease_type
        item['suggestion'] = suggestion
        item['bed'] = bed
        
        yield item

