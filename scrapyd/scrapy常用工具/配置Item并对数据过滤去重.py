#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapyd.items import ScrapydItem
from scrapy.exceptions import DropItem
"""
1、在pipeline中实现相关的类
如果使用scrapy genspider spidername domain,则会自动创建pipeline类
(1)一个Item Pipeline不需要继承特定基类，只需要实现某些特定方法，例如process_item、open_spider、close_spider。 
(2)一个Item Pipeline必须实现一个process_item(item, spider)方法，该方法用来处理每一项由Spider爬取到的数据，其中的两个参数： 　
    Item　爬取到的一项数据（Item或字典）。 　
    Spider　爬取此项数据的Spider对象。

"""
class PriceConverterPipeline(object):

    # 英镑兑换人民币汇率
    exchange_rate = 8.5309

    def process_item(self, item, spider):
        # 提取item的price字段,去掉前面的"$",转换为float类型,乘以汇率
        price = float(item['price'][1:]) * self.exchange_rate

        # 保留2为小数,赋值回item的price字段
        item['price'] = '¥%.2f' % price
        return item

"""
2、启用Item Pipeline
在scrapy中,Item pipeline是可选组件,想启用某个Item Pipeline,需要在配置文件setting.py中进行配置
"""

ITEM_PIPELINES = {
   'scrapyd.pipelines.PriceConverterPipeline': 300,
}

"""
3、在Item Pipeline过滤重复数据
使用DropItem去重
"""

class DuplicationPipeline(object):
    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['name']
        if name in self.book_set:
            raise DropItem("Duplicate book found: %s" % item)
        self.book_set.add(name)

        return item
