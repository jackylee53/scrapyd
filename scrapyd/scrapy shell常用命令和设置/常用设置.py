#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
1、禁用Cookie
修改settings.py文件#COOKIES_ENABLED = False配置项,去掉注释,False为禁止Cookie,禁止调用本地Cookie,可以防止通过
用户Cookie信息对用户进行分析和识别的网站把爬虫禁掉
2、设置下载时延
修改settings.py文件#DOWNLOAD_DELAY = 3配置项,3代表3秒,支持0.5等格式。
3、使用IP池
(1)通过http://www.xicidaili.com/查找常用代理IP信息,在settings.py中添加如下信息：
IPPOOL=[
{"ipaddr":"121.33.226.167:3128"},
{"ipaddr":"118.187.10.11:80"}
]
(2)设置下载中间件信息
与代理服务器相关的下载中间件是HttpProxyMiddleware,同样在Scrapy官方文档中,HttpProxyMiddleware对应类为：
class scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware
如下：
(3)setting中做响应的设置
修改downloader如下：DOWNLOADER_MIDDLEWARES = {
    # 'scrapyd.middlewares.ScrapydDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 123,
    'scrapyd.middlewares.IPPOOLS': 125,
}

"""

# middlewares下载中间件
# 导入随机数模块,目的是从IPPOOL中挑选一个IP
import random

# 从setting文件中引入设置好的IP
from scrapyd.settings import IPPOOL

# 导入官方文档HttpProxyMiddleware对应的模块
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    def __init__(self, ip=''):
        self.ip = ip
    # process_request方法进行请求处理
    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print("当前使用的IP是" + thisip["ipaddr"])
        request.meta["proxy"] = "http://" + thisip["ipaddr"]
