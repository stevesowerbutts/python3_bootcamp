# Script to test scrapy (Installed in venv)
# https://books.toscrape.com/

import scrapy

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css(".price_color::text").extract_first(),
                'title': article.css('h3 > a::attr(title)').extract_first(),
            }

        next = response.css('.next > a::attr(href)').extract_first()
        if next is not None:
            yield response.follow(next, self.parse)
