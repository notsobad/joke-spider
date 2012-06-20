# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.contrib.exporter import JsonLinesItemExporter
class FmlPipeline(object):
	'''
	def __init__(self):
		self.file = open('data2.json', 'w')
		self.exporter = JsonLinesItemExporter(self.file)
		self.exporter.start_exporting()
	'''
	def open_spider(self, spider):
		name = "%s.json" % spider.name
		self.file = open(name, 'w')
		self.exporter = JsonLinesItemExporter(self.file)
		self.exporter.start_exporting()
	
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
