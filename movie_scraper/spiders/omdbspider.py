from __future__ import absolute_import
import scrapy
import json


class OMDBSpider(scrapy.Spider):
    """ Spider that crawls OMDB's API for categorical film data. """

    name = "omdbspider"
    allowed_domains = ["www.omdbapi.com/"]

    """ Replace the API field with api_key. """
    url = "http://www.omdbapi.com/?t={}&apikey={}"
    url = url.format('{}', "3e6165e0")

    start_urls = [
    ]

    def parse(self, response):
        return


