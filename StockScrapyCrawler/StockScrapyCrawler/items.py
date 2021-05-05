# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockscrapycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    industry_category = scrapy.Field()
    stock_id = scrapy.Field()
    type = scrapy.Field()
    verify = scrapy.Field()
