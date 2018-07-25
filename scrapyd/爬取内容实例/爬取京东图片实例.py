#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

def crawl(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pattern1 = '<div id="plist".+?<div class="page clearfix">'
    result1 = re.compile(pattern1).findall(html1)
    print("result1", result1)
    result0 = result1[0]
    print("result0", result0)
    pattern2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imagelist = re.compile(pattern2).findall(result0)
    print("imagelist", imagelist)
    x = 1
    for imageurl in imagelist:
        imagename = "/Users/jacky/Downloads/" + str(page) + str(x) + '.jpg'
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.HTTPError as e:
            if hasattr(e, "code"):
                x = x + 1
                print(e.code)
            if hasattr(e, "reason"):
                x = x + 1
                print(e.reason)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x = x + 1
                print(e.code)
            if hasattr(e, "reason"):
                x = x + 1
                print(e.reason)
        x = x + 1

for i in range(1,79):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    crawl(url, i)