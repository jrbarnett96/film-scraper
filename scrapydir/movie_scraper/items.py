# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


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