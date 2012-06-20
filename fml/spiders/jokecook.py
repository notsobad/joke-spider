from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from fml.items import FmlItem
import pprint
import urlparse
import os
import sys 
import re


class MySpider(CrawlSpider):
	name = 'waduanzi'
	allowed_domains = ['waduanzi.com']
	start_urls = ["http://www.waduanzi.com/duanzi-1"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		url = hxs.select('//div[@id="page-nav"]//li[@class="next"]/a/@href').extract()[0]

		url = urlparse.urljoin(response.url, url)
		self.log(url)
		yield Request(url, callback=self.parse)
		
		for p in hxs.select('//div[@class="waterfall-item"]/p/a/text()').extract():
			cont = re.sub(r'<[^>]*?>', '', p)
			yield FmlItem(cont=cont, url='')
