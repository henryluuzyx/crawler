# -*- coding: utf-8 -*-
import datetime
import os
import socket
import time

import scrapy
from scrapy import signals
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from basic.items import BasicItem


class BroadSpider(CrawlSpider):
    name = 'broad'
    allowed_domains = [
        'baomoi.com',
        'vietnamnet.vn',
        'vnexpress.net',
        'tinhte.vn',
        'tuoitre.vn',
        'thanhnien.vn',
        'dantri.com.vn'
    ]
    start_urls = [
        'http://www.baomoi.com/',
        'http://vietnamnet.vn/',
        'http://vnexpress.net/',
        'https://tinhte.vn/',
        'http://tuoitre.vn/',
        'http://thanhnien.vn/',
        'http://dantri.com.vn/'
    ]

    page_count = 0
    data_path = 'data'
    try:
        os.makedirs(data_path)
    except Exception:
        pass
    start_time = time.time()

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[not(starts-with(@href, "#"))]'),
             callback='parse_item', follow=True),
    )

    def closed(self, reason):
        self.end_time = time.time()
        request_bytes = self.crawler.stats.get_value('downloader/request_bytes')
        response_bytes = self.crawler.stats.get_value('downloader/response_bytes')

        with open(os.path.join(self.data_path, 'log.txt'), 'ab') as f:
            print>>f, 'Total time elapsed: {}s'.format(
                                                self.end_time - self.start_time)
            print>>f, 'Request bytes: {}'.format(request_bytes)
            print>>f, 'Response bytes: {}'.format(response_bytes)

    def parse_item(self, response):
        self.page_count += 1
        if self.page_count == 5001:
            with open(os.path.join(self.data_path, 'log.txt'), 'ab') as f:
                print>>f, 'Time to crawl and download 5000 pages: {}s'.format(
                                                time.time() - self.start_time)

        # Write HTML content to a file
        with open(os.path.join(self.data_path, str(self.page_count)), 'wb') as f:
            print>>f, response.body
        # A file contains URLs of all visited pages
        with open(os.path.join(self.data_path, 'downloadList.txt'), 'ab') as f:
            print>>f, response.url

        # DO SOME SCRAPING HERE...
        l = ItemLoader(item=BasicItem(), response=response)

        # Set values for housekeeping fields
        l.add_value('url', response.url)

        return l.load_item()
