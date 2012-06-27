from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from fml.items import FmlItem, JokeItem
import pprint
import urlparse
import os
import sys 
import re


class MySpider(CrawlSpider):
	name = 'sickipedia'
	allowed_domains = ['sickipedia.org']
	start_urls = ["http://www.sickipedia.org/getjokes/all?page=1&sortcolumn=age&direction=asc&l=1"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		m = re.search(r'all\?page=(\d+)&', response.url)
		page = m.groups()[0]
		next_page = int(page) + 1

		url = urlparse.urljoin(response.url, '?page=%s&sortcolumn=age&direction=asc&l=1' % next_page)
		self.log(url)
		yield Request(url, callback=self.parse)
		
		for div in hxs.select('//div[@class="content"]/div[contains(@id, "joke")]'):
			cont = "\n".join( div.select('div/table//td[1]/text()').extract() )
			cont = re.sub(r'<[^>]*?>', '', cont)
			cont = cont.strip()

			tags = div.select('div/span[3]/a/text()').extract()
			try:
				score = div.select('div/span[7]/text()').extract()[0]
				score = int(float(score.replace(',', '')))
			except:
				score = 0

			yield JokeItem(cont=cont, url='', tags=tags, score=score)

