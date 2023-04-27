from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apps.home.content_scraper import FinnCarSpider

def run_crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl(FinnCarSpider)
    process.start()
