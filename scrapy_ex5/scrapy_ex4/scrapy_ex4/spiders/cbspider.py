#-*- coding: utf-8 -*-
import sys
sys.path.append("..")

from scrapy.selector import Selector
from scrapy.spiders import Spider


from ..items import FjsenItem
itemcount = 0
class FjsenSpider(Spider):


    name="fjsen"
    allowed_domains=["fjsen.com"]
    start_urls=['http://www.fjsen.com/j/node_94962_'+str(x)+'.htm' for x in range(2,11)]+['http://www.fjsen.com/j/node_94962.htm']
    def parse(self,response):
        global itemcount
        hxs = Selector(response)
        sites=hxs.select('//ul/li')
        items=[]
        for site in sites:
            item=FjsenItem()
            item['title']=site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['addtime']=site.select('span/text()').extract()
            if item['addtime']:
              itemcount =  itemcount +1
              print itemcount
              items.append(item)
        return items