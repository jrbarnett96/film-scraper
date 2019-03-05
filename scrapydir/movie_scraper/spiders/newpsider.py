from __future__ import absolute_import
import scrapy
#from scrapy.crawler import CrawlerProcess
import bs4
#from scrapydir.movie_scraper.items import MovieScrapingItem

class MovieScrapingItem(scrapy.Item):
    """
    Data structure containing movie_scraper fields
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

class newpsider(scrapy.Spider):
    """
    Spider
    """
    name = "mojopspider"
    allowed_domains = ["boxofficemojo.com/"]
    start_urls = [
        "http://www.boxofficemojo.com/alltime/world/",
    ]

    def parse(self, response):
        """
        This is where the fun begins
        """

        # ***This section is independent of Scrapy*****
        films = []
        table = bs4.BeautifulSoup(str(response.body), features="lxml")
        # "table" is bs4 type
        table_row_all = table.findAll("tr")[2:]  # slice removes non table text
        tds_all = []

        for html_row in table_row_all:
            tds_all.append([td.get_text() for td in html_row.findAll("td")])
        # ^^^^This section is independent of Scrapy^^^^^

        # Converting 2d array into Scrapy Item
        for film in tds_all[1:]:  # removes categories row
            boitem = MovieScrapingItem()
            for i in range(len(boitem.varlist)):
                boitem[str(boitem.varlist[i])] = film[i]
            yield boitem

if __name__ == "__main__":
    boitem = MovieScrapingItem()
    boitem['title'] = "test"
    print(boitem["title"])
