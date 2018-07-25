#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import http.cookiejar
url = "http://news.163.com/18/0706/14/DM1QG745000189FH.html"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "http://news.163.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
# 设置cookie
cjar = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))

headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read()
fhandle = open("E:/test/test.html", "wb")
fhandle.write(data)
fhandle.close()