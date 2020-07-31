from scrapy.loader import ItemLoader
import bs4
import requests
import scrapy
from ..items import MovieItem

# working relatively, except troublesome import


class FilmSpider(scrapy.Spider):
    """ Scrapes financial data from BoxOfficeMojo's all-time world record page. """

    name = "FilmSpider"
    allowed_domains = ["boxofficemojo.com/"]
    start_urls = [
        "https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW",
    ]

    def parse(self, response):
        """ From each film row in the alltime list, parses a film's financial data into an Item. """

        """ Load web page, find all instances of table rows. """
        record_table = bs4.BeautifulSoup(response.body, features="lxml").find("table")
        rt_categories = [b.text.strip() for b in record_table.find("tr").find_all("th")]

        def get_table_rows(table):
            """Given a table, returns all its rows"""
            rows = []
            for tr in table.find_all("tr")[1:]:
                cells = []
                # grab all td tags in this table row
                tds = tr.find_all("td")
                if len(tds) == 0:
                    # if no td tags, search for th tags
                    # can be found especially in wikipedia tables below the table
                    ths = tr.find_all("th")
                    for th in ths:
                        cells.append(th.text.strip())
                else:
                    # use regular td tags
                    for td in tds:
                        cells.append(td.text.strip())
                rows.append(cells)
            return rows

        rt_data = get_table_rows(record_table)


        """ Reshape categories for easier indexing. """
        rt_categories = [rt_categories[i].lower() for i in range(0, len(rt_categories))]
        rt_categories[2] =  "worldwide"
        rt_categories[3] = "domestic"
        rt_categories[4] = 'domestic_share'
        rt_categories[5] = 'overseas'
        rt_categories[6] = 'overseas_share'

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
        """

        """ For each row in the table, create an Item using ItemLoader. """
        for row in rt_data:
            row_data = row
            film_record = MovieItem()

            """ Add columns according to the corresponding column name in RT_CATEGORIES. """
            for i in range(len(row_data)):
                film_record[rt_categories[i]] = row_data[i]

            """ Query OMDB API for categorical data, store response in dictionary format. """
            film_title = "+".join(row_data[1].split())
            omdb_query = "http://www.omdbapi.com/?apikey=3e6165e0&t={}".format(film_title)
            omdb_response = requests.get(omdb_query).json()
            film_record['categorical_data'] = omdb_response

            yield film_record
