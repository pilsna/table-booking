from scrapy.spider import Spider
from scrapy.selector import Selector


class RestaurantSpider(Spider):
    name = "restaurant"
    allowed_domains = ["dinnerbooking.com"]
    start_urls = [
        "http://dinnerbooking.com/search",
        "http://dinnerbooking.com/search/search/1/"
    ]

    def parse(self, response):
        sel = Selector(response)
        restaurants = sel.xpath("//div[@class='list_content']")
        for restaurant in restaurants:
            name = restaurant.xpath('h3/a[@class="search_restaurant_name"]/text()').extract()[0]
            url = restaurant.xpath('h3/a[@class="search_restaurant_name"]/@href').extract()[0]
            location = restaurant.xpath('h4/text()').extract()[0]

            time_table = list()
            link_times = restaurant.xpath('div[@class="list_times"]//a/text()')
            for time_link in link_times:
                time_table.append(time_link.extract())

            output = dict(
                restaurant_name=name,
                restaurant_address=location,
                restaurant_url=url,
                time_table=time_table
            )

            return output