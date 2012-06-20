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
	name = 'tduanzi'
	allowed_domains = ['tduanzi.com']
	start_urls = ["http://www.tduanzi.com/tweets/?tps=1"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		page = hxs.select('//div[@class="black2"]/span[@class="disabled"]/text()').extract()[0]
		next_page = int(page) + 1

		url = urlparse.urljoin(response.url, "?tps=1&page=%s" % next_page)
		self.log(url)
		yield Request(url, callback=self.parse)
		
		for p in hxs.select('//div[@class="list"]//div[@class="right"]/a/text()').extract():
			cont = re.sub(r'<[^>]*?>', '', p)
			yield FmlItem(cont=cont, url='')
