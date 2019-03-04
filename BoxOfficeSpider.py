import scrapy
from scrapy.crawler import CrawlerProcess
import bs4

class BoxOfficeItem(scrapy.Item):
    """
    Data structure containing stuff
    """
    rank = scrapy.Field()
    title = scrapy.Field()
    studio = scrapy.Field()
    worldwide = scrapy.Field()
    domestic = scrapy.Field()
    domestic_share = scrapy.Field()
    overseas = scrapy.Field()
    overseas_share = scrapy.Field()
    year = scrapy.Field()

    varlist = ("rank", "title", "studio", "worldwide", "domestic", "domestic_share",
            "overseas", "overseas_share", "year")

    def __print__(self):
        print(self.keys(), self.values())

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

        table = bs4.BeautifulSoup(str(response.body), features="lxml")
        # "table" is bs4 type
        table_row_all = table.findAll("tr")[2:]  # slice removes non table text
        tds_all = []

        for html_row in table_row_all:
            tds_all.append([td.get_text() for td in html_row.findAll("td")])
        films = []
        for film in tds_all[1:]:  # removes categories row
            boitem = BoxOfficeItem()
            for i in range(len(boitem.varlist)):
                boitem[str(boitem.varlist[i])] = film[i]
            films.append(boitem)
            for film in films:
                print(film)

# running the spider
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(BoxOfficeSpider)
process.start() # the script will block here until the crawling is finished