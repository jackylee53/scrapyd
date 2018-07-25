#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
《非打印字符》
符号 | 含义
\n  | 用于匹配换行符
\t  | 用于匹配制表符
"""
import re
pattern = "\n"
string = '''http://www.baidu.com
http://www.sina.com.cn'''
result = re.search(pattern, string)
print(result)
'''--<_sre.SRE_Match object; span=(20, 21), match='\n'>--'''

"""
《通用字符》
符号  |   含义
\w   |   匹配任意一个字母、数字或下划线
\W   |   匹配除字母、数字或下划线外的任意一个字符
\d   |   匹配任意一个十进制数
\D   |   匹配除十进制数以外的任意一个其他字符
\s   |   匹配任意一个空白字符
\S   |   匹配除空白字符外的任意一个其他字符
"""
import re
pattern = "\w\dpython\w"
string = "abcdfphp345python_py"
result = re.search(pattern, string)
print(result)
'''--<_sre.SRE_Match object; span=(9, 18), match='45python_'>--'''

"""
《原子表》
原子表由[]表示，它定义了一组地位平等的原子,匹配的时候会取该原子表中任意一个原子进行匹配，如[abc]可以匹配a、b、c其中任意一个字符；
[^]代表的是除了中括号里面的原子均可以匹配
"""
import re
pattern1 = "\w\dpython[xyz]\w"
pattern2 = "\w\dpython[^xyz]\w"
pattern3 = "\w\dpython[xyz]\W"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
print(result1)
'''--<_sre.SRE_Match object; span=(9, 19), match='45pythony_'>--'''
print(result2)
'''--None--'''
print(result3)
'''--None--'''