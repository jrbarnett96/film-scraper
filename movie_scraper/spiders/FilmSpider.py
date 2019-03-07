from __future__ import absolute_import
import scrapy
# from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from movie_scraper.items import *
import bs4
import requests

# working relatively, except troublesome import


class FilmSpider(scrapy.Spider):
    """ Scrapes financial data from BoxOfficeMojo's all-time world record page. """

    name = "mojospider"
    allowed_domains = ["boxofficemojo.com/"]
    start_urls = [
        "http://www.boxofficemojo.com/alltime/world/",
    ]

    def parse(self, response):
        """ From each film row in the alltime list, parses a film's financial data into an Item. """

        """ Load web page, find all instances of table rows. """
        record_page = bs4.BeautifulSoup(str(response.body), "html.parser")
        record_table = record_page.findAll("tr")
        rt_categories = record_table[2].findAll("a")
        rt_data = record_table[3:]

        """ Reshape categories for easier indexing. """
        rt_categories = [rt_categories[i].string.lower() for i in range(len(rt_categories))]
        rt_categories[5] = 'domestic_share'
        rt_categories[7] = 'overseas_share'
        rt_categories[8] = 'year'

        """ For each row in the table, create an Item using ItemLoader. """
        for row in rt_data:
            row_data = row.findAll("td")
            film_record = ItemLoader(MovieItem(), response=response)

            """ Add columns according to the corresponding column name in RT_CATEGORIES. """
            for i in range(len(row_data)):
                film_record.add_value(rt_categories[i], row_data[i].string)

            """ Query OMDB API for categorical data, store response in dictionary format. """
            film_title = "+".join(row_data[1].string.split())
            omdb_query = "http://www.omdbapi.com/?apikey=3e6165e0&t={}".format(film_title)
            omdb_response = requests.get(omdb_query).json()
            film_record.add_value('categorical_data', omdb_response)

            yield film_record.load_item()
