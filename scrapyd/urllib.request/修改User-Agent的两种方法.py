#!/usr/bin/python
# -*- coding: utf-8 -*-

## 1、使用build_opener()修改包头
import urllib.request
url = 'https://blog.csdn.net/bit_kaki/article/details/80869548'
headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

fhandle=open('/Users/jacky/Downloads/3.html','wb')
fhandle.write(data)
fhandle.close()

## 2、使用add_header()添加包头
import urllib.request
url = 'https://blog.csdn.net/bit_kaki/article/details/80869548'
req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
data = urllib.request.urlopen(req).read()