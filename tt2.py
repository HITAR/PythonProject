#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


# 1. 验证Email
# someone@gmail.com
# bill.gates@microsoft.com
s1 = 'someone.@gmail.com'
s2 = 'bill.gates@microsoft.com'
pattern = r'^[0-9a-z\_\.]+@[0-9a-z]+\.[a-z]+$'
re_email = re.compile(pattern)
print('matched: \'%s\'' % re_email.match(s1).group(0))
print('matched: \'%s\'' % re_email.match(s2).group(0))
'''
matched: 'someone@gmail.com'
matched: 'bill.gates@microsoft.com'
'''


# 2. 验证并提取出带名字的Email地址
# <Tom Paris> tom@voyager.org
s = '<Tom Paris> tom@voyager.org'
pattern = r'^<([a-zA-Z]+)\s+[a-zA-Z]+>\s+([0-9a-z\_\.]+@[0-9a-z]+\.[a-z]+)$'
re_email = re.compile(pattern)
m = re_email.match(s)
print('%s\'s email: %s' % (m.group(1), m.group(2)))
'''
Tom's email: tom@voyager.org
'''