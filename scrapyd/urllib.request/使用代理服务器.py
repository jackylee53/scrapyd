#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
代理服务器地址:http://www.xicidaili.com/
"""

def user_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandle({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

proxy_addr = "101.236.60.52:8866"
data = user_proxy(proxy_addr, "http://www.baidu.com/s?wd=")
print(len(data))