import scrapy


class TopUsCompaniesSP500Item(scrapy.Item):
    rank = scrapy.Field()
    company = scrapy.Field()
    year = scrapy.Field()
    market_cap = scrapy.Field()
