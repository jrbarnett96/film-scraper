import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
import json
import requests
from scrapy.utils.log import configure_logging

class BoxOfficeSpider(scrapy.Spider):
    name = "boxoffice"
    start_urls = [
        "www.boxofficemojo.com/alltime/world/",
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        with open('test.txt', 'w') as f:
            f.write("hello")

#running without command line
#configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()
d = runner.crawl(BoxOfficeSpider)

d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished