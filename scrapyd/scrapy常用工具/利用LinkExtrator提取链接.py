#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
利用LinkExtrator创建链接
在spiders中新增解析链接权限,具体方法如下

"""
import scrapy
from scrapy.linkextractors import LinkExtractor

class BookSpider(scrapy.Spider):

    """.....
    """

    def parse(self, response):
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)

"""
LinkExtractor的其他用法：

现在有了实验环境，先说明一种特例情况，LinkExtractor构造器的所有参数都有默认值，如果构造对象时不传递任何参数（使用默认值），就提取页面中所有链接。以下代码将提取页面example1.html中的所有链接：      
>>> from scrapy.linkextractors import LinkExtractor      
>>> le = LinkExtractor()      
>>> links = le.extract_links(response1)      
>>> [link.url for link in links]      
['http://example1.com/intro/install.html',      
'http://example1.com/intro/tutorial.html',      
'http://example1.com/../examples.html',      
'http://stackoverflow.com/tags/scrapy/info',      
'https://github.com/scrapy/scrapy'] 


下面依次介绍LinkExtractor构造器的各个参数：

●　allow 接收一个正则表达式或一个正则表达式列表，提取绝对url与正则表达式匹配的链接，如果该参数为空（默认），就提取全部链接。 
示例　提取页面example1.html中路径以/intro开始的链接：      
>>> from scrapy.linkextractors import LinkExtractor      
>>> pattern = '/intro/.+\.html$'      
>>> le = LinkExtractor(allow=pattern)      
>>> links = le.extract_links(response1)      
>>> [link.url for link in links]      
['http://example1.com/intro/install.html',      
'http://example1.com/intro/tutorial.html'] 

●　deny 接收一个正则表达式或一个正则表达式列表，与allow相反，排除绝对url与正则表达式匹配的链接。 
示例　提取页面example1.html中所有站外链接（即排除站内链接）：      
>>> from scrapy.linkextractors import LinkExtractor      
>>> from urllib.parse import urlparse
>>> pattern = patten = '^' + urlparse(response1.url).geturl()      
>>> pattern      '^http://example1.com'      
>>> le = LinkExtractor(deny=pattern)      
>>> links = le.extract_links(response1)      
>>> [link.url for link in links]      
['http://stackoverflow.com/tags/scrapy/info',       
'https://github.com/scrapy/scrapy'] 

●　allow_domains 接收一个域名或一个域名列表，提取到指定域的链接。 
示例　提取页面example1.html中所有到github.com和stackoverflow.com这两个域的链接：      
>>> from scrapy.linkextractors import LinkExtractor      
>>> domains = ['github.com', 'stackoverflow.com']      
>>> le = LinkExtractor(allow_domains=domains)      
>>> links = le.extract_links(response1)      
>>> [link.url for link in links]      
['http://stackoverflow.com/tags/scrapy/info',       
'https://github.com/scrapy/scrapy']

●　deny_domains 接收一个域名或一个域名列表，与allow_domains相反，排除到指定域的链接。 
示例　提取页面example1.html中除了到github.com域以外的链接：      
>>> from scrapy.linkextractors import LinkExtractor      
>>> le = LinkExtractor(deny_domains='github.com')      
>>> links = le.extract_links(response1)      
>>> [link.url for link in links]      
['http://example1.com/intro/install.html',       
'http://example1.com/intro/tutorial.html',       
'http://example1.com/../examples.html',       
'http://stackoverflow.com/tags/scrapy/info'] 

●　restrict_xpaths 接收一个XPath表达式或一个XPath表达式列表，提取XPath表达式选中区域下的链接。 
示例　提取页面example1.html中<div id="top">元素下的链接：
>>> from scrapy.linkextractors import LinkExtractor      
>>> le = LinkExtractor(restrict_xpaths='//div[@id="top"]')      
>>> links = le.extract_links(response1)      
>>> [link.url for link in links]      
['http://example1.com/intro/install.html',      
'http://example1.com/intro/tutorial.html',      
'http://example1.com/../examples.html'] 

●　restrict_css 接收一个CSS选择器或一个CSS选择器列表，提取CSS选择器选中区域下的链接。 
示例　提取页面example1.html中<div id="bottom">元素下的链接：      
>>> from scrapy.linkextractors import LinkExtractor      
>>> le = LinkExtractor(restrict_css='div#bottom')      
>>> links = le.extract_links(response1)      
>>> [link.url for link in links]      
['http://stackoverflow.com/tags/scrapy/info',       
'https://github.com/scrapy/scrapy'] 

●　tags 接收一个标签（字符串）或一个标签列表，提取指定标签内的链接，默认为['a', 'area']。

●　attrs 接收一个属性（字符串）或一个属性列表，提取指定属性内的链接，默认为['href']。 
示例　提取页面example2.html中引用JavaScript文件的链接：      
>>> from scrapy.linkextractors import LinkExtractor      
>>> le = LinkExtractor(tags='script', attrs='src')      
>>> links = le.extract_links(response2)      
>>> [link.url for link in links]      
['http://example2.com/js/app1.js',       
'http://example2.com/js/app2.js'] 

●　process_value 接收一个形如func(value)的回调函数。如果传递了该参数，LinkExtractor将调用该回调函数对提取的每一个链接（如a的href）进行处理，回调函数正常情况下应返回一个字符串（处理结果），想要抛弃所处理的链接时，返回None。 
示例　在页面example2.html中，某些a的href属性是一段JavaScript代码，代码中包含了链接页面的实际url地址，此时应对链接进行处理，提取页面example2.html中所有实际链接：

>>> import re      
>>> def process(value):      
...       m = re.search("javascript:goToPage\('(.*?)'", value)      
...       # 如果匹配，就提取其中url 并返回，不匹配则返回原值      
...       if m:      
...           value = m.group(1)      
...       return value      
>>> from scrapy.linkextractors import LinkExtractor      
>>> le = LinkExtractor(process_value=process)      
>>> links = le.extract_links(response2)      
>>> [link.url for link in links]      
['http://example2.com/home.html',      
'http://example2.com/doc.html',      
'http://example2.com/example.html'] 

到此，我们介绍完了LinkExtractor构造器的各个参数，实际应用时可以同时使用一个或多个参数描述提取规则，这里不再举例。
"""