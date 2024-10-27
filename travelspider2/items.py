import scrapy
#定义需要爬取数据的数据结构
class TravelspiderItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    review_count = scrapy.Field()
