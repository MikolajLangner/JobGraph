# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboardItem(scrapy.Item):
    role = scrapy.Field()
    stack = scrapy.Field()
