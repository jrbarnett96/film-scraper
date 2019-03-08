from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

process = CrawlerProcess(get_project_settings())

process.crawl('FilmSpider')
process.start()



data = []
with open('films.json') as f:
    for line in f:
        data.append(json.loads(line))

for elements in data:
    print(elements)