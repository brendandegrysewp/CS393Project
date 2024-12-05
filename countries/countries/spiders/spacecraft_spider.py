from pathlib import Path

import scrapy
from countries.items import SpacecraftItem

class SpacecraftSpider(scrapy.Spider):
    name = "spacecraft"

    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_fictional_spacecraft"
    ]
    #    def start_requests(self):
        #        for url in urls:
        #    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = SpacecraftItem()
        for row in response.xpath('//li/i/text()').getall():
            item['model'] = row
            yield item
