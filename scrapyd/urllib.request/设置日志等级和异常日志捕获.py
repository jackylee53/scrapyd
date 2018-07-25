#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.error
"""设置日志级别"""
httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httphd, httpshd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen("http://edu.51cto.com")
print("data", data)

"""捕获异常日志"""
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.HTTPError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)