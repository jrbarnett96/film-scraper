from __future__ import absolute_import
import scrapy
import json
from movie_scraper.items import jsonItem

# incomplete
# if you want to try xpath instead of bs4
# https://www.simplified.guide/scrapy/scrape-table

# in the future we can try to transition out of requests and bs4 and go all
# scrapy

class omdbspider(scrapy.Spider):
    """
    Spider
    """
    name = "omdbspider"
    allowed_domains = ["www.omdbapi.com/"]

    """ Replace the API field with api_key. """
    url = "http://www.omdbapi.com/?t={}&apikey={}"
    url = url.format('{}', "3e6165e0")

    start_urls = [
        url,
    ]

def parse(self, response):
    # omdbapi returns json
    jsonresponse = json.loads(response.body_as_unicode())

    # assignment to scrapy item
    item = jsonItem()
    item["json"] = jsonresponse

    return item


