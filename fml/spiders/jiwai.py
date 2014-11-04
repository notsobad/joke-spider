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
	name = 'jiwai'
	allowed_domains = ['3jy.com']
	start_urls = ["http://www.3jy.com/youmo/index.html"]

	def parse(self, response):
		hxs = response.selector
		
		for joke in hxs.xpath('//div[contains(@id, "content-")]/div[@class="c"]'):
			cont = '\n'.join(joke.xpath('.//text()').extract()).strip()
			yield FmlItem(cont=cont, url='')

		url = hxs.xpath('//a[@id="nex_page"]/@href').extract()[0]
		url = urlparse.urljoin(response.url, url)

		yield Request(url, callback=self.parse)
