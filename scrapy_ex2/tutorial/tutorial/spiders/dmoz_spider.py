__author__ = 'frank1'
import scrapy
from ..items import TutorialItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    #allowed_domains = ["ibm.com"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        #"http://www.ibm.com/developerworks/cn/opensource/",
        #"http://www.ibm.com/developerworks/cn/web/"
    ]

    # version 1:
    # def parse(self, response):
    #     filename = response.url.split("/")[-2] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)


    # version 2:
    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         title = sel.xpath('a/text()').extract()
    #         link = sel.xpath('a/@href').extract()
    #         desc = sel.xpath('text()').extract()
    #         print title, link, desc


    def parse(self, response):
      for sel in response.xpath('//ul/li'):
         item = TutorialItem()
         item['title'] = sel.xpath('a/text()').extract()
         item['link'] = sel.xpath('a/@href').extract()
         item['desc'] = sel.xpath('text()').extract()
         yield item