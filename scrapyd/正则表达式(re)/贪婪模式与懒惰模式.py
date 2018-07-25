#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
pattern1 = "p.*y"
pattern2 = "p.*?y"
string = "abcdfphp345Pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1)
'''--<_sre.SRE_Match object; span=(5, 21), match='php345Pythony_py'>--'''
print(result2)
'''--<_sre.SRE_Match object; span=(5, 13), match='php345Py'>--'''

