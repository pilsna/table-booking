# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import requests

GEO_API_URL = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find/"


class RestaurantItem(Item):
    # define the fields for your item here like:
    name = Field()
    address = Field()
    latitude = Field()
    longitude = Field()
    url = Field()
    time_table = Field()

    def address_to_lat_lng(self):
        """
            Use arcigis.com API to get latitude and longitude from the Address.
        """
        if len(self['address']) <= 3:
            return

        payload = {'text': self['address'], 'f': 'pjson'}
        r = requests.get(GEO_API_URL, params=payload)
        data = r.json()
        if "locations" in data.keys():
            coords = data['locations'][0]['feature']['geometry']
            self["latitude"] = coords['x']
            self["longitude"] = coords['y']
