# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FmlItem(Item):
    # define the fields for your item here like:
    # name = Field()
	cont = Field()
	url = Field()

class JokeItem(Item):
	cont = Field()
	url = Field()
	tags = Field()
	score = Field()
