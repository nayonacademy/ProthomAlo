# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://www.prothomalo.com/archive/2018-01-07',
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # print "I AM PROTHOM ALO"
        # print page
        # print response
        # res = response.css('.listing div a.link_overlay').extract()
        # print res
        count = 0
        c2 = 0
        for i in response.css('.listing div a.link_overlay::attr(href)').extract():
            # yield {
            #     'link': 'http://www.prothomalo.com'
            # }
            # print 'http://www.prothomalo.com' + i
            url = 'http://www.prothomalo.com' + i
            # yield {
            #         'link': 'http://www.prothomalo.com'+str(i)
            #     }

            yield scrapy.Request(url=url, callback=self.parse_inner)
            count +=1

            next_page = response.css('a.next_page::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
                c2 +=1
        print count
        print c2
    def parse_inner(self,response):
        # print "I am here"
        # innercon = response.css('article div p::text').extract()
        for i in response.css('article div p::text').extract():
            print i
        # print innercon
        # for i in response.css('.col-xs-12.search-results-listing a::attr(href)').extract():
        #     yield {
        #         'link': 'https://radiopaedia.org'+str(i)
        #     }
        #
        #     next_page = response.css('a[rel~="next"]::attr(href)').extract_first()
        #     if next_page is not None:
        #         next_page = response.urljoin(next_page)
        #         yield scrapy.Request(next_page, callback=self.parse)

# scrapy crawl quotes