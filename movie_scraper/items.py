# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst



class MovieItem(scrapy.Item):
    """ Custom Item representing a row in Box Office Mojo's record table. """

    rank = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    studio = scrapy.Field(output_processor=TakeFirst())
    worldwide = scrapy.Field(output_processor=TakeFirst())
    domestic = scrapy.Field(output_processor=TakeFirst())
    domestic_share = scrapy.Field(output_processor=TakeFirst())
    overseas = scrapy.Field(output_processor=TakeFirst())
    overseas_share = scrapy.Field(output_processor=TakeFirst())
    year = scrapy.Field(output_processor=TakeFirst())

    categorical_data = scrapy.Field(output_processor=TakeFirst())


class JsonItem(scrapy.Item):
    """
    Data structure containing movie_scraper fields
    """
    json = scrapy.Field()


if __name__ == "__main__":
    item = MovieScraperItem()
    print(item.fields)
