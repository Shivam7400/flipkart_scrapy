# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FlipkartScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    original_price = scrapy.Field()
    price_off_percentages = scrapy.Field()
    image_url = scrapy.Field()