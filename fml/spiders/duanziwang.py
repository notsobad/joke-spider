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
	name = 'duanziwang'
	allowed_domains = ['duanziwang.com']
	start_urls = ["http://www.duanziwang.com/"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		url = hxs.select('//ol[@class="page-navigator"]/li/a[@class="next"]/@href').extract()[0]
		url = urlparse.urljoin(response.url, url)
		self.log(url)
		yield Request(url, callback=self.parse)
		
		for post in hxs.select('//div[@class="post f"]'):
			p = "".join(post.select('p/text()').extract())
			cont = re.sub(r'<[^>]*?>', '', p)
			yield FmlItem(cont=cont, url='')
