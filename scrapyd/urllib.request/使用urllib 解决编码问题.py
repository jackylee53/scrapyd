#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
url = "http://www.baidu.com/s?wd="
key = "江南"
key_code = urllib.request.quote(key)
all_key = url + key_code
req = urllib.request.Request(all_key)
data = urllib.request.urlopen(req).read()
fb = open("/Users/jacky/Downloads/test.html","wb")
fb.write(data)
fb.close()