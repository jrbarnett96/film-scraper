# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    """ Custom Item representing a row in Box Office Mojo's record table. """

    """ Box Office Mojo data. """
    rank = scrapy.Field()
    title = scrapy.Field()
    studio = scrapy.Field()
    worldwide = scrapy.Field()
    domestic = scrapy.Field()
    domestic_share = scrapy.Field()
    overseas = scrapy.Field()
    overseas_share = scrapy.Field()
    year = scrapy.Field()

    """ OMDB data. """
    categorical_data = scrapy.Field()


class JsonItem(scrapy.Item):
    """
    Data structure containing movie_scraper fields
    """
    json = scrapy.Field()

