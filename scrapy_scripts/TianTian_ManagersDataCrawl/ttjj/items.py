# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TtjjItem(scrapy.Item):
    # define the fields for your item here like:

    TOTALDAYS = scrapy.Field()
    MGRID = scrapy.Field()