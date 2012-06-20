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
	name = 'fml'
	allowed_domains = ['fmylife.com']
	start_urls = ["http://www.fmylife.com/?page=1293"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)

		# bug in page: http://www.fmylife.com/?page=1293
		#url = hxs.select('//div[@class="pagination"]/ul[@class="right"]/li[2]/a/@href').extract()[0]
		page = int(response.url.split('?page=')[1])
		url = urlparse.urljoin(response.url, "?page=%s" % (page+1))
		self.log(url)
		yield Request(url, callback=self.parse)
		
		
		for p in hxs.select('//div[@class="post article"]/p').extract():
			cont = re.sub(r'<[^>]*?>', '', p)
			yield FmlItem(cont=cont)
