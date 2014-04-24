#!/bin/bash

#This command will generate the items.json
#with all the details about the restaurants ( see RestaurantItem structure )
scrapy crawl restaurant -o items.json -t json