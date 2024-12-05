#Made by following the tutorial at https://docs.scrapy.org/en/2.11/intro/tutorial.html
from pathlib import Path

import scrapy
from countries.items import CountriesItem

class CountrySpider(scrapy.Spider):
    name = "country"
    start_urls = [ "https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government" ]

    # def start_requests(self):
    #     url = "https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government"
    #     print(url)
    #     yield scrapy.Request(url, callback=self.parse)

    #    def start_requests(self):
        #        for url in urls:
        #    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = CountriesItem()
        for row in response.xpath('//table[3]/tbody/tr'):
            item["country"] = row.xpath('th/a/text()').get()
            item["position"] = row.xpath('td/a[1]/text()').get()
            item["name"] = row.xpath('td/a[2]/text()').get()
            yield item
