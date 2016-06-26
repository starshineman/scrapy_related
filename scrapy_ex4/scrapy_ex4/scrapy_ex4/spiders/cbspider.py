#-*- coding: utf-8 -*-
import sys
sys.path.append("..")
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ..items import FjsenItem
class FjsenSpider(BaseSpider):

    #self.itemcount = 0
    name="fjsen"
    allowed_domains=["fjsen.com"]
    start_urls=['http://www.fjsen.com/j/node_94962_'+str(x)+'.htm' for x in range(2,11)]+['http://www.fjsen.com/j/node_94962.htm']
    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//ul/li')
        items=[]
        for site in sites:
            item=FjsenItem()
            item['title']=site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['addtime']=site.select('span/text()').extract()
            if item['addtime']:
              # self.itemcount =  self.itemcount +1
              print 1
              items.append(item)
        return items