# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class BoxOfficeMojoPipeline(object):
    """ Pipeline for processing Items scraped from Box Office Mojo"""

    def process_item(self, item, spider):
        if item.get('categorical_data')['Response'] == 'False':
            raise DropItem
        else:
            """ Cast numerical data into floats. """
            item['worldwide'] = float(item['worldwide'][1:])
            item['domestic'] = float(item['domestic'][1:])
            item['domestic_share'] = float(item['domestic_share'][:-1])
            item['overseas'] = float(item['overseas'][1:])
            item['overseas_share'] = float[item['overseas_share'][1:]]
            if len(item['year']) > 4:
                item['year'] = item['year'][:-1]
            return item


class OMDBPipeline(object):
    """ Pipeline for processing categorical data from OMDB, reinserting the processed data. """

    def process_item(self, item, spider):
        if item.get('categorical_data')['Response'] == 'False':
            raise DropItem
        else:
            categorical = item.get('categorical_data')
