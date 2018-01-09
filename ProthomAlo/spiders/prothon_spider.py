# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://www.prothomalo.com/archive/2018-01-07',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in response.css('.listing div a.link_overlay::attr(href)').extract():
            url = 'http://www.prothomalo.com' + i

            yield scrapy.Request(url=url, callback=self.parse_inner)

            next_page = response.css('a.next_page::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
    def parse_inner(self,response):
        for i in response.css('article div p::text').extract():
            yield {
                'text': i
            }


# command line
# scrapy crawl quotes
# for write in json format
#scrapy crawl quotes -o quotes.json