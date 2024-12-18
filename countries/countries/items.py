# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountriesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    country = scrapy.Field()
    position = scrapy.Field()
    
class SpacecraftItem(scrapy.Item):
    # define the fields for your item here like:
    model = scrapy.Field()