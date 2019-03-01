import scrapy
from scrapy.crawler import CrawlerProcess

class DmozItem(scrapy.Item):
    """
    Data structure containing stuff
    """
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class BoxOfficeSpider(scrapy.Spider):
    """
    Spider
    """
    name = "boxoffice"
    allowed_domains = ["boxofficemojo.com/"]
    start_urls = [
        "http://www.boxofficemojo.com/alltime/world/",
    ]

    def parse(self, response):
        """
        This is where the fun begins
        """
        tr_elements = response.xpath('//tr')
        yield tr_elements


# running the spider
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(BoxOfficeSpider)
process.start() # the script will block here until the crawling is finished