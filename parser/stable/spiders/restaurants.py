from scrapy.spider import Spider
from scrapy.selector import Selector
from stable.items import RestaurantItem

class RestaurantsSpider(Spider):
    name = "restaurants"
    allowed_domains = ["dinnerbooking.com"]
    start_urls = [
        "http://dinnerbooking.com/search/search/1/",
        "http://dinnerbooking.com/search/search/2/",
        "http://dinnerbooking.com/search/search/3/"
        "http://dinnerbooking.com/search/search/4/",
        "http://dinnerbooking.com/search/search/5/",
        "http://dinnerbooking.com/search/search/6/"
    ]

    __addresses = list()

    def parse(self, response):
        sel = Selector(response)
        restaurants = sel.xpath("//div[@class='list_content']")
        for restaurant in restaurants:

            n = restaurant.xpath('h3/a[@class="search_restaurant_name"]/text()').extract()[0]
            u = restaurant.xpath('h3/a[@class="search_restaurant_name"]/@href').extract()[0]
            a = restaurant.xpath('h4/text()').extract()[0]

            #Avoid duplicates
            if a in self.__addresses:
                continue
            else:
                self.__addresses.append(a)

            the_restaurant = RestaurantItem()
            the_restaurant['name'] = n
            the_restaurant['url'] = u
            the_restaurant['address'] = a

            the_restaurant.address_to_lat_lng()
            yield the_restaurant