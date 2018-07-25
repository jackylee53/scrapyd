#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
实现Item Pipeline,将数据存入MongoDB
1、Pipeline实现写入mongodb的方法
2、在settings.py中启用MongoDBPipeline,在如下参数中增加：
ITEM_PIPELINES = {
        'example.pipelines.PriceConverterPipeline': 300,
        'example.pipelines.MongoDBPipeline': 400,
}

3、使用settings配置文件
在Pipeline中加载@claassmethod方法
在settings.py中配置
MONGO_DB_URI = 'mongodb://192.168.1.105:27017/'
MONGO_DB_NAME = 'liushuo_scrapy_data'
"""

from scrapy.item import Item
import pymongo

class MongoDBPipeline(object):
    # 数据库的URL地址,名字
    DB_URL = 'mongodb://localhost:27017/'
    DB_NAME = 'scrapy_data'

    # @classmethod
    # def from_crawler(cls, crawler):
    #     cls.DB_URI = crawler.settings.get('MONGO_DB_URI', 'mongodb:localhost:27017/')
    #     cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'scrapy_data')
    #     return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item

