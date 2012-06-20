# Scrapy settings for fml project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'fml'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['fml.spiders']
NEWSPIDER_MODULE = 'fml.spiders'
ITEM_PIPELINES = ["fml.pipelines.FmlPipeline"]
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5'
COOKIES_ENABLED = False
