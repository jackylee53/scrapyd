#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
多数网站采用http post方式进行用户认证,用户认证后cookie保存在浏览器本地,方可爬取登录后的页面
(1)导入cookie处理模块http.cookier
(2)使用http.cookiejar.CookieJar()创建CookieJar对象
(3)使用HTTPCookieProcessor创建cookie处理器,并以它为参数构建opener对象
(4)创建全局默认的opener对象
"""

import urllib.request
import urllib.parse
import http.cookiejar
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LCBs8"
postdata = urllib.parse.urlencode({
    "formhash": "cec074ec",
    "referer": "http://bbs.chinaunix.net/",
    "username": "weisuen",
    "password": "aA123456",
    "loginsubmit": "true"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
file = open("/Users/jacky/Downloads/test1.html", 'wb')
file.write(data)
file.close()

url2 = "http://bbs.chinaunix.net"
data2 = urllib.request.urlopen(url2).read()
fb = open("/Users/jacky/Downloads/test2.html", 'wb')
fb.write(data2)
fb.close()
