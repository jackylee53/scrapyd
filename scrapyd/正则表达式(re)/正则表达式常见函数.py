#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
1、re.match()
从源字符串的起始位置匹配一个模式,re.match()的使用格式：re.match(pattern, string, flag)
"""
import re
pattern = ".python"
string = "apythonhellomypythonhispythonourpythonend"
result1 = re.match(pattern, string)
print(result1)
'''--<_sre.SRE_Match object; span=(0, 7), match='apython'>--'''
result2 = re.match(pattern, string).span()
print(result2)
'''--(0, 7)--'''

"""
2、re.search()
re.search()从全文进行匹配，re.match()从源字符串的开头进行匹配
"""
import re
pattern = ".python."
string = "abcpythonhellomypythonhispythonourpythonend"
result1 = re.match(pattern, string)
print(result1)
'''--None--'''
result2 = re.search(pattern, string)
print(result2)
'''--<_sre.SRE_Match object; span=(2, 10), match='cpythonh'>--'''

"""
3、全局匹配函数re.findall()
将符合模式的匹配条件都匹配出来
使用方法：(1)使用re.compile()对正则表达式解析进行预编译;(2)编译后,使用findall()根据正则表达式从源字符串中将匹配结果全部找到
"""
import re
string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.")
result = pattern.findall(string)
print(result)
'''--['ypythonh', 'spythono', 'rpythone']--'''

"""
4、re.sub()
根据正则表达式来实现某些字符串替换的功能
re.sub()函数的格式：re.sub(pattern, rep, string, max)
"""
import re
pattern = "python"
string = "hellomypythonhispythonourpythonend"
result1 = re.sub(pattern, "php", string)
print(result1)
'''--hellomyphphisphpourphpend--'''
result2 = re.sub(pattern, "php", string, 2)
print(result2)
'''--hellomyphphisphpourpythonend--'''
