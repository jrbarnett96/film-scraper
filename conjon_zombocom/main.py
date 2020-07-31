from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':

    #utils.create_data_folder()
    
    process = CrawlerProcess(get_project_settings())

    process.crawl('FilmSpider')
    process.start()

