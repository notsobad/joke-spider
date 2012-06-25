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
	name = 'jokecook'
	allowed_domains = ['jokecook.com']
	start_urls = ["http://www.jokecook.com/"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		url = hxs.select('//div[@class="navigation"]/p/a[contains(text(), "Older")]/@href').extract()[0]

		url = urlparse.urljoin(response.url, url)
		self.log(url)
		yield Request(url, callback=self.parse)
		
		for p in hxs.select('//div[@class="postcontent"]/p').extract():
			cont = re.sub(r'<[^>]*?>', ' ', p)
			cont = re.sub(r'Via @[^\ ]*', '', cont)
			cont = re.sub(r'#[^\ ]*', '', cont)
			yield FmlItem(cont=cont.strip(), url='')
