# -*- coding: utf-8 -*-
import scrapy
from gip.items import GipItem

class IpinfoSpider(scrapy.Spider):
    name = "ipinfo"
    allowed_domains = ["ipinfo.io"]
    start_urls = ['http://ipinfo.io/AS15169']

    def parse(self, response):
        for temp in response.xpath('//*[@id = "content"]/section/table[2]'):

            for url1 in temp.xpath('tr[@class = "hidden"]/td[1]/a'):
                item = GipItem()
                item['ip'] = url1.xpath('@href').extract()[0]
                #print(url1.xpath('@href').extract()[0][9:])
                yield item



