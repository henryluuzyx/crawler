# -*- coding: utf-8 -*-
import scrapy


class BasicItem(scrapy.Item):
    # Housekeeping fields
    url = scrapy.Field()
