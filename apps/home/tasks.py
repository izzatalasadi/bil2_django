from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .content_scraper import FinnCarSpider

@shared_task
def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(FinnCarSpider)
    process.start()
