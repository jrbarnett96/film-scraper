BOT_NAME = 'Bot'
ITEM_PIPELINES = {
    'BoxOfficeSpider.JsonPipeline': 1,
    'BoxOfficeSpider.CsvPipeline': 1,
}
#SPIDER_MODULES = ['BoxOfficeSpider.py']