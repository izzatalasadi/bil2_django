import os

import scrapy
from scrapy.exceptions import DropItem


class FinnCar(scrapy.Item):
    km = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    model = scrapy.Field()
    model_type = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()


class FinnCarSpider(scrapy.Spider):
    name = 'finn_car'
    allowed_domains = ['finn.no']
    start_urls = [
        'https://www.finn.no/pw/search/car-norway?orgId=783850227',  # start URL for the spider
    ]
    # delete old cars.csv file if it exists
    if os.path.exists("cars.csv"):
        os.remove("cars.csv")

    # custom settings for the spider
    custom_settings = {
        "FEED_FORMAT": "csv",  # save data in CSV format
        "FEED_URI": "cars.csv",  # name of CSV file to save data
        # user agent
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }

    def __init__(self, *args, **kwargs):
        super(FinnCarSpider, self).__init__(*args, **kwargs)
        self.seen_cars = set()

    def parse(self, response):
        # Get car listings from current page
        counter = 0
        for car in response.xpath('//div[@class="inner r-pal"]'):
            if not "Solgt" in str(car.xpath('.//span/text()').extract()[0]):
                item = FinnCar()
                # Use relative XPath expressions to select details line
                line = str(car.xpath('.//h3/text()').extract()
                           [0]).replace("-", "").replace(",", "").split()
                item['km'] = "".join(line[-6:-4])
                item['price'] = "".join(line[-2:])
                item['year'] = line[-7]
                item['model'] = line[0]
                item['model_type'] = line[1]
                item['url'] = car.xpath('//a/@href').extract()[counter]
                item['image'] = car.xpath('//img/@src').extract()[counter]
                counter += 1

                # Check if car is already seen
                car_key = f"{item['model']}_{item['url']}"
                if car_key in self.seen_cars:
                    raise DropItem(f"Duplicate car found: {car_key}")
                else:
                    self.seen_cars.add(car_key)
                    yield item

        # Follow pagination links
        next_page = response.xpath('//a[@class="pam"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
