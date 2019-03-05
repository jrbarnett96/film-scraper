from __future__ import absolute_import
import scrapy
#from scrapy.crawler import CrawlerProcess
import bs4
from movie_scraper.items import * #let it be, necessary for now with scrapy

# working relatively, except troublesome import
# in future convert section noted below away from bs4 and to xpath

class mojospider(scrapy.Spider):
    """
    Spider
    """
    name = "mojospider"
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
            boitem = MovieScraperItem()
            for i in range(len(boitem.fields)):
                boitem[str(boitem.varlist[i])] = film[i]
            yield boitem

if __name__ == "__main__":
    boitem = MovieScraperItem()
    boitem['title'] = "test"
    print(boitem["title"])
