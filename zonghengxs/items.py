# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import *


def handle_content(value):
    value = re.sub(r'</p>', "", value)
    value = re.sub(r'<p>|<div.*>|</div>', "\n", value)
    return value


class ZonghengxsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    details = scrapy.Field(
        input_processor=MapCompose(handle_content)
    )


class ZonghengxsItemLoader(ItemLoader):

    default_output_processor = TakeFirst()

