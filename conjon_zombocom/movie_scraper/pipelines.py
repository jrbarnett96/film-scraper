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
            numerical_cats = ['worldwide', 'domestic', 'overseas']
            for i in numerical_cats:
                item[i] = float(item[i][1:].replace(",", ""))
            percent_cats = ['domestic_share', 'overseas_share']
            for j in percent_cats:
                item[j] = float(item[j][:-1])
            if len(item['year']) > 4:
                item['year'] = item['year'][:-1]
            return item


class OMDBPipeline(object):
    """ Pipeline for processing categorical data from OMDB,
    reinserting the processed data. """

    def process_item(self, item, spider):
        if item.get('categorical_data')['Response'] == 'False':
            raise DropItem
        else:
            """ Retrieve the OMDB dictionary from the MovieItem. """
            categorical = item.get('categorical_data')

            """ Remove extraneous categories. """
            categories_to_remove = ['Language', 'Country', 'Poster', 'DVD',
                                    'Type', 'Website', 'Response',
                                    'Title', 'Year', 'BoxOffice']
            for i in categories_to_remove:
                categorical.pop(i)

            """ Cast numerical data into floats. """
            categorical['Runtime'] = float(categorical['Runtime'].split()[0])
            categorical['Genre'] = categorical['Genre'].split(', ')
            categorical['Metascore'] = float(categorical['Metascore'])
            categorical['imdbRating'] = float(categorical['imdbRating'])
            categorical['imdbVotes'] = float("".join(categorical['imdbVotes'].split(',')))

            item_dict = dict(item)
            item_dict.pop('categorical')
            for i in categorical.keys():
                item_dict[i] = categorical[i]

            return item_dict
