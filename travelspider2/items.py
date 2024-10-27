import scrapy

class TravelspiderItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    review_count = scrapy.Field()
