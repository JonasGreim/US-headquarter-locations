# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopuscompanieslocationscraperItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    company = scrapy.Field()
    revenues = scrapy.Field()
    profits = scrapy.Field()
    year = scrapy.Field()