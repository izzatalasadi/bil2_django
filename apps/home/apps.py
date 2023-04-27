from django.apps import AppConfig
from django.db.models import BigAutoField
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .content_scraper import FinnCarSpider


class MyAppConfig(AppConfig):
    name = 'apps.home'
    DEFAULT_AUTO_FIELD = BigAutoField
    