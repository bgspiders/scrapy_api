#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：scrapy_api 
@File    ：demo.py
@IDE     ：PyCharm 
@INFO     ： 
@Author  ：BGSPIDER
@Date    ：19/11/2024 上午11:37 
'''
from api.API import ScrapydAPI
scrapyd = ScrapydAPI('http://localhost:6800')
project='crawl'
spider='crawl_html'
# scrapyd.schedule(project, spider, id=id)
job_id=scrapyd.schedule(project, spider)
print(job_id)
print(scrapyd.job_info(project,job_id))
