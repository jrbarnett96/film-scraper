import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.selector import Selector

class BoxOfficeSpider(scrapy.Spider):
    name = "boxoffice"
    start_urls = [
        "www.boxofficemojo.com/alltime/world/",
    ]

    def parse(self, response):
        print(Selector(response=response).xpath('//title/text()').get())

#running without command line
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()
d = runner.crawl(BoxOfficeSpider)

d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished