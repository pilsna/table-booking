# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from geojson import Point
import requests

GEO_API_URL = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find/"


class RestaurantItem(Item):
    # define the fields for your item here like:
    name = Field()
    address = Field()
    geometry = Field()
    url = Field()

    def address_to_lat_lng(self):
        """
            Use arcigis.com API to get latitude and longitude from the Address.
        """
        correct_address = self['address'][:self['address'].index(",")]
        correct_address += ", Copenhagen"

        payload = {'text': self['address'], 'f': 'pjson'}
        r = requests.get(GEO_API_URL, params=payload)
        data = r.json()
        if "locations" in data.keys():
            coords = data['locations'][0]['feature']['geometry']
            self["geometry"] = Point((coords['x'], coords['y']))
