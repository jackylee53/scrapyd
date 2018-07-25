#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
《常见原字符及其含义》
符号  |   含义
.    |   匹配除换行符以外的任意字符
^    |   匹配字符串开始位置
$    |   匹配字符串结束位置
*    |   匹配0次、1次或多次前面的原子
?    |   匹配0次或1次前面的原子
+    |   匹配1次或多次前面的原子
{n}  |   前面的原子恰好出现n次
{n,} |   前面的原子至少出现n次
{n,m}|   前面的原子至少出现n次,最多出现m次
|    |   模式选择符
()   |   模式单元符
"""

"""
1、任意匹配元字符
符号  |   含义
.    |   匹配除换行符以外的任意字符
"""
import re
pattern = ".python..."
string = "abcdfphp345pythony_py"
result = re.search(pattern, string)
print(result)
'''--<_sre.SRE_Match object; span=(10, 20), match='5pythony_p'>--'''

"""
2、边界限制元字符
符号  |   含义
^    |   匹配字符串开始位置
$    |   匹配字符串结束位置
"""
import re
pattern1 = "^abd"
pattern2 = "^abc"
pattern3 = "py$"
pattern4 = "ay$"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
print(result1)
'''--None--'''
result2 = re.search(pattern2, string)
print(result2)
'''--<_sre.SRE_Match object; span=(0, 3), match='abc'>--'''
result3 = re.search(pattern3, string)
print(result3)
'''--<_sre.SRE_Match object; span=(19, 21), match='py'>--'''
result4 = re.search(pattern4, string)
print(result4)
'''--None--'''

"""
3、边界限制元字符
符号  |   含义
*    |   匹配0次、1次或多次前面的原子
?    |   匹配0次或1次前面的原子
+    |   匹配1次或多次前面的原子
{n}  |   前面的原子恰好出现n次
{n,} |   前面的原子至少出现n次
{n,m}|   前面的原子至少出现n次,最多出现m次
"""
import re
pattern1 = "py.*n"
pattern2 = "cd{2}"
pattern3 = "cd{3}"
pattern4 = "cd{2,}"
string = "abcdddfphp345pythony_py"
result1 = re.search(pattern1, string)
print(result1)
'''--<_sre.SRE_Match object; span=(13, 19), match='python'>--'''
result2 = re.search(pattern2, string)
print(result2)
'''--<_sre.SRE_Match object; span=(2, 5), match='cdd'>--'''
result3 = re.search(pattern3, string)
print(result3)
'''--<_sre.SRE_Match object; span=(2, 6), match='cddd'>--'''
result4 = re.search(pattern4, string)
print(result4)
'''--<_sre.SRE_Match object; span=(2, 6), match='cddd'>--'''

"""
4、模式选择符
符号  |   含义
|    |   模式选择符
"""
import re
pattern = "python|php"
string = "abcdfphp345pythony_py"
result = re.search(pattern, string)
print(result)
'''--<_sre.SRE_Match object; span=(10, 20), match='5pythony_p'>--'''

"""
5、模式单元符号
符号  |   含义
()    |   模式单元符号
"""
import re
pattern1 = "(cd){1,}"
pattern2 = "cd{1,}"
string = "abcdcdcdcdfphp345pythony_py"
result1 = re.search(pattern1, string)
print(result1)
'''--<_sre.SRE_Match object; span=(2, 10), match='cdcdcdcd'>--'''
result2 = re.search(pattern2, string)
print(result2)
'''--<_sre.SRE_Match object; span=(2, 4), match='cd'>--'''