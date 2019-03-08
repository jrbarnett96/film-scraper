from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import jsonreader

process = CrawlerProcess(get_project_settings())

process.crawl('FilmSpider')
process.start()

for i in jsonreader.readjson("films.json"):
    print(i)