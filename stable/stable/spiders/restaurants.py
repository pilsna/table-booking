from scrapy.spider import Spider
from scrapy.selector import Selector
from stable.items import RestaurantItem

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
            the_restaurant = RestaurantItem()

            n = restaurant.xpath('h3/a[@class="search_restaurant_name"]/text()').extract()[0]
            u = restaurant.xpath('h3/a[@class="search_restaurant_name"]/@href').extract()[0]
            a = restaurant.xpath('h4/text()').extract()[0]

            time_table = list()
            link_times = restaurant.xpath('div[@class="list_times"]//a/text()')
            for time_link in link_times:
                time_table.append(time_link.extract())


            the_restaurant['name'] = n
            the_restaurant['url'] = u
            the_restaurant['address'] = a
            the_restaurant['time_table'] = time_table

            the_restaurant.address_to_lat_lng()
            yield the_restaurant