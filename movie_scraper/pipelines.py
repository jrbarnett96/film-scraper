# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# to my understanding, we later implement the joining of both spiders output
# as part of the pipeline

import json


class BoxOfficeMojoPipeline(object):
    """ Pipeline for processing Items scraped from Box Office Mojo box office records. """

    def process_item(self, item, spider):
        return

    def open_spider(self, spider):
        return

    def close_spider(self, spider):
        return
