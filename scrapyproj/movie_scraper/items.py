# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# id like to be able to fix the script in mojospider as tonot ahve to rely
# on varlist, which is really just a workaround. attempting to iterate
# through MovieScraperItem.fields gives them out of order, and the
# return from mojo's table is an ordered, unlabeled list
# what we could do is go through the mojo's returned lists and convert each
# to a dictionary as field:listvalue.

class MovieScraperItem(scrapy.Item):
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

        varlist = (
        "rank", "title", "studio", "worldwide", "domestic", "domestic_share",
        "overseas", "overseas_share", "year")


class jsonItem(scrapy.Item):
    """
    Data structure containing movie_scraper fields
    """
    json = scrapy.Field()


if __name__ == "__main__":
    item = MovieScraperItem()
    print(item.fields)