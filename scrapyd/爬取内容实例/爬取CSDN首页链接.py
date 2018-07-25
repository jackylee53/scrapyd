#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

def geturl(url):
    header = ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [header]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    pattern = '(https?://[^\s)";]+\.(\w|/))'
    link = re.compile(pattern).findall(data)
    link = list(set(link))
    return link

url = "https://www.csdn.net/"
linkurls = geturl(url)
for linkurl in linkurls:
    print(linkurl)

