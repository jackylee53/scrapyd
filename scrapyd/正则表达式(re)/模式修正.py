#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
《模式修正符》
符号  |   含义
I    |   匹配时忽略大小写
M    |   匹配多行
L    |   做本地化识别匹配
U    |   根据Unicode字符及解析字符
S    |   让"."匹配包括换行符,即用了该模式修正后,"."可以匹配任意字符
"""

import re
pattern = "python"
string = "abcdfphp345Pythony_py"
result1 = re.search(pattern, string)
result2 = re.search(pattern, string, re.I)
print("result1", result1)
'''--result1 None--'''
print("result2", result2)
'''--result2 <_sre.SRE_Match object; span=(11, 17), match='Python'>--'''

string3 = "abcdefphp345pythony_pypython123456"
result3 = re.findall(pattern, string3, re.M)
print(result3)
'''--['python', 'python']--'''