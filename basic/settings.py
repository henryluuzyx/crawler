# -*- coding: utf-8 -*-
BOT_NAME = 'basic'

SPIDER_MODULES = ['basic.spiders']
NEWSPIDER_MODULE = 'basic.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

LOG_LEVEL = 'INFO'

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 15

CLOSESPIDER_ITEMCOUNT = 5000

CONCURRENT_REQUESTS = 256
CONCURRENT_REQUESTS_PER_DOMAIN = 32
REACTOR_THREADPOOL_MAXSIZE = 20

COOKIES_ENABLED = False

# Setting for breadth-first order crawler
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

HTTPERROR_ALLOWED_CODES = [301]
