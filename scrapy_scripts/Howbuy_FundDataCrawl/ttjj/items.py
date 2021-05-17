# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TtjjItem(scrapy.Item):
    # define the fields for your item here like:
    code  = scrapy.Field()
    date = scrapy.Field()
    jd_20_4 = scrapy.Field()
    jd_20_3 = scrapy.Field()
    jd_20_2 = scrapy.Field()     
    jd_20_1 = scrapy.Field()     
    jd_19_4 = scrapy.Field()
    jd_19_3 = scrapy.Field()
    jd_19_2 = scrapy.Field()     
    jd_19_1 = scrapy.Field()     

    nd_20 = scrapy.Field()
    nd_19 = scrapy.Field()
    nd_18 = scrapy.Field()
    nd_17 = scrapy.Field()
    nd_16 = scrapy.Field()
    nd_15 = scrapy.Field()
    nd_14 = scrapy.Field()
    nd_13 = scrapy.Field()
