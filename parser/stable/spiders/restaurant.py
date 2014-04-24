from scrapy.spider import Spider
from scrapy.selector import Selector
from stable.items import RestaurantTimeTableItme

class RestaurantSpider(Spider):
    name = "restaurant"
    allowed_domains = ["dinnerbooking.com"]
    start_urls = []

    def parse(self, response):
        sel = Selector(response)

        time_table = list()
        link_times = sel.xpath('//li[@class="list_times"]//a/text()')
        for time_link in link_times:
            time_table.append(time_link.extract())

        sel.xpath('//h2[@id="title"]/text()')[0].extract()

        table_item = RestaurantTimeTableItme()
        table_item['restaurant_address'] = name
        table_item['time_table'] = time_table

        return table_item